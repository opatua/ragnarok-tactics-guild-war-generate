from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import ProductFamily
from duapola_admin.forms import ProductFamilyForm


class ProductFamilyDataView(BaseDatatableView):
    model = ProductFamily
    columns = [
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
                'product_family_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'product_family_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(ProductFamilyDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(slug__icontains=search)
            )
        return qs


class ProductFamilyListView(TemplateView):
    template_name = "product_family/index.html"


class ProductFamilyCreateView(CreateView):
    model = ProductFamily
    template_name = "product_family/create.html"
    form_class = ProductFamilyForm
    success_url = reverse_lazy("product_family_index")


class ProductFamilyUpdateView(UpdateView):
    model = ProductFamily
    template_name = "product_family/update.html"
    form_class = ProductFamilyForm
    success_url = reverse_lazy("product_family_index")


class ProductFamilyDeleteView(DeleteView):
    model = ProductFamily
    template_name = "product_family/delete.html"
    success_url = reverse_lazy("product_family_index")
