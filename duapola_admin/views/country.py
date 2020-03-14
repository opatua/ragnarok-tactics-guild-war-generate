from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import Country
from duapola_admin.forms import CountryForm


class CountryDataView(BaseDatatableView):
    model = Country
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
                'country_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'country_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(CountryDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class CountryListView(TemplateView):
    template_name = "country/index.html"


class CountryCreateView(CreateView):
    model = Country
    template_name = "country/create.html"
    form_class = CountryForm
    success_url = reverse_lazy("country_index")


class CountryUpdateView(UpdateView):
    model = Country
    template_name = "country/update.html"
    form_class = CountryForm
    success_url = reverse_lazy("country_index")


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "country/delete.html"
    success_url = reverse_lazy("country_index")
