from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Character, Team
from ragnarok.forms import CharacterForm, TeamFormset


class CharacterDataView(BaseDatatableView):
    model = Character
    columns = [
        'name',
        'updated_at',
        'manage',
    ]

    def render_column(self, row, column):
        if column == 'manage':
            update_link = reverse_lazy(
                'character_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'character_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(CharacterDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )

        return qs.order_by('-updated_at')


class CharacterListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'character/index.html'


class CharacterCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/form.html'
    form_class = CharacterForm
    success_url = reverse_lazy('character_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            CharacterCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['teams'] = TeamFormset(
                self.request.POST
            )
        else:
            context['teams'] = TeamFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        teams = context['teams']
        with transaction.atomic():
            self.object = form.save()

            if teams.is_valid():
                teams.instance = self.object
                teams.save()
        return super(CharacterCreateView, self).form_valid(form)


class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/form.html'
    form_class = CharacterForm
    success_url = reverse_lazy('character_index')

    def get_context_data(self, **kwargs):
        context = super(
            CharacterUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['teams'] = TeamFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['teams'] = TeamFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        teams = context['teams']
        with transaction.atomic():
            self.object = form.save()
            if teams.is_valid():
                teams.instance = self.object
                teams.save()
        return super(CharacterUpdateView, self).form_valid(form)


class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/delete.html'
    success_url = reverse_lazy('character_index')

    def delete(self, request, *args, **kwargs):
        Team.objects.filter(character_id=kwargs.get('pk')).delete()

        return super().delete(request, *args, **kwargs)
