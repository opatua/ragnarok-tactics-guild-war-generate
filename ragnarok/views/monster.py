from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Monster, MonsterElement
from ragnarok.forms import MonsterForm, MonsterElementFormset


class MonsterDataView(BaseDatatableView):
    model = Monster
    columns = [
        'name',
        'faction',
        'manage',
    ]

    def render_column(self, row, column):
        if column == 'manage':
            update_link = reverse_lazy(
                'monster_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'monster_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(MonsterDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class MonsterListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'monster/index.html'


class MonsterCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Monster
    template_name = 'monster/form.html'
    form_class = MonsterForm
    success_url = reverse_lazy('monster_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            MonsterCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['monster_elements'] = MonsterElementFormset(
                self.request.POST
            )
        else:
            context['monster_elements'] = MonsterElementFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        MonsterElements = context['monster_elements']
        with transaction.atomic():
            self.object = form.save()

            if MonsterElements.is_valid():
                MonsterElements.instance = self.object
                MonsterElements.save()
        return super(MonsterCreateView, self).form_valid(form)


class MonsterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Monster
    template_name = 'monster/form.html'
    form_class = MonsterForm
    success_url = reverse_lazy('monster_index')

    def get_context_data(self, **kwargs):
        context = super(
            MonsterUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['monster_elements'] = MonsterElementFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['monster_elements'] = MonsterElementFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        MonsterElements = context['monster_elements']
        with transaction.atomic():
            self.object = form.save()
            if MonsterElements.is_valid():
                MonsterElements.instance = self.object
                MonsterElements.save()
        return super(MonsterUpdateView, self).form_valid(form)


class MonsterDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Monster
    template_name = 'monster/delete.html'
    success_url = reverse_lazy('monster_index')

    def delete(self, request, *args, **kwargs):
        MonsterElement.objects.filter(monster_id=kwargs.get('pk')).delete()

        return super().delete(request, *args, **kwargs)
