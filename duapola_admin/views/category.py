from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import Category
from duapola_admin.forms import CategoryForm


class CategoryDataView(BaseDatatableView):
    model = Category
    columns = [
        'name',
        'parent_category',
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
                'category_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'category_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(CategoryDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(slug__icontains=search) |
                Q(parent_category__name__icontains=search) |
                Q(parent_category__slug__icontains=search)
            )
        return qs


class CategoryListView(TemplateView):
    template_name = "category/index.html"


class CategoryCreateView(CreateView):
    model = Category
    template_name = "category/create.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_index")


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category/update.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_index")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/delete.html"
    success_url = reverse_lazy("category_index")
