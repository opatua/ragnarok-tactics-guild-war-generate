from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Character
from ragnarok.forms import CharacterForm, TeamFormset


class CharacterDataView(BaseDatatableView):
    model = Character
    columns = [
        'name',
        'created_at',
        'updated_at',
        'manage',
    ]

    def render_column(self, row, column):
        if column == 'created_at':
            date = row.created_at
            return date.strftime('%Y-%m-%d %H:%M')
        if column == 'updated_at':
            date = row.updated_at
            return date.strftime('%Y-%m-%d %H:%M')
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
        return qs


class CharacterListView(TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'character/index.html'


class CharacterCreateView(CreateView):
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


class CharacterUpdateView(UpdateView):
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


class CharacterDeleteView(DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/delete.html'
    success_url = reverse_lazy('character_index')
