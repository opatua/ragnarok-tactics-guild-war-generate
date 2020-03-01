from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import Product
from duapola_admin.forms import ProductForm


class ProductDataView(BaseDatatableView):
    model = Product
    columns = [
        'name',
        'sku',
        'quantity',
        'price',
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
                'product_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'product_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(ProductDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(slug__icontains=search)
            )
        return qs


class ProductListView(TemplateView):
    template_name = "product/index.html"


class ProductCreateView(CreateView):
    model = Product
    template_name = "product/create.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_index")


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "product/update.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_index")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/delete.html"
    success_url = reverse_lazy("product_index")
