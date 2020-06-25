from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Essence
from ragnarok.forms import EssenceForm


class EssenceDataView(BaseDatatableView):
    model = Essence
    columns = [
        'name',
        'type',
        'element',
        'manage'
    ]

    def render_column(self, row, column):
        if column == 'manage':
            update_link = reverse_lazy(
                'essence_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'essence_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(EssenceDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class EssenceListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = "essence/index.html"


class EssenceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = "essence/create.html"
    form_class = EssenceForm
    success_url = reverse_lazy("essence_index")


class EssenceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = "essence/update.html"
    form_class = EssenceForm
    success_url = reverse_lazy("essence_index")


class EssenceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = "essence/delete.html"
    success_url = reverse_lazy("essence_index")
