from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_backend.models import Color
from duapola_admin.forms import ColorForm


class ColorDataView(BaseDatatableView):
    model = Color
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
                'color_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'color_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(ColorDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(slug__icontains=search)
            )
        return qs


class ColorListView(TemplateView):
    template_name = "color/index.html"


class ColorCreateView(CreateView):
    model = Color
    template_name = "color/create.html"
    form_class = ColorForm
    success_url = reverse_lazy("color_index")


class ColorUpdateView(UpdateView):
    model = Color
    template_name = "color/update.html"
    form_class = ColorForm
    success_url = reverse_lazy("color_index")


class ColorDeleteView(DeleteView):
    model = Color
    template_name = "color/delete.html"
    success_url = reverse_lazy("color_index")
