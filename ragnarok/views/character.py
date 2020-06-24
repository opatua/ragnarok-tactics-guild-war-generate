from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Character
from ragnarok.forms import CharacterForm


class CharacterDataView(BaseDatatableView):
    model = Character
    columns = [
        'name',
        'point',
        'created_at',
        'updated_at',
        'manage'
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
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/create.html'
    form_class = CharacterForm
    success_url = reverse_lazy('character_index')


class CharacterUpdateView(UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/update.html'
    form_class = CharacterForm
    success_url = reverse_lazy('character_index')


class CharacterDeleteView(DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Character
    template_name = 'character/delete.html'
    success_url = reverse_lazy('character_index')
