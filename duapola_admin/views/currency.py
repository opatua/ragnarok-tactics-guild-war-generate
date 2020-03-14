from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import Currency
from duapola_admin.forms import CurrencyForm


class CurrencyDataView(BaseDatatableView):
    model = Currency
    columns = [
        'id',
        'name',
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
                'currency_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'currency_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(CurrencyDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class CurrencyListView(TemplateView):
    template_name = "currency/index.html"


class CurrencyCreateView(CreateView):
    model = Currency
    template_name = "currency/create.html"
    form_class = CurrencyForm
    success_url = reverse_lazy("currency_index")


class CurrencyUpdateView(UpdateView):
    model = Currency
    template_name = "currency/update.html"
    form_class = CurrencyForm
    success_url = reverse_lazy("currency_index")


class CurrencyDeleteView(DeleteView):
    model = Currency
    template_name = "currency/delete.html"
    success_url = reverse_lazy("currency_index")
