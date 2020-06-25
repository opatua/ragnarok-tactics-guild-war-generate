from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Essence, EssenceElement
from ragnarok.forms import EssenceForm, EssenceElementFormset


class EssenceDataView(BaseDatatableView):
    model = Essence
    columns = [
        'name',
        'type',
        'manage',
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
    template_name = 'essence/index.html'


class EssenceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = 'essence/form.html'
    form_class = EssenceForm
    success_url = reverse_lazy('essence_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            EssenceCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['essence_elements'] = EssenceElementFormset(
                self.request.POST
            )
        else:
            context['essence_elements'] = EssenceElementFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        essence_elements = context['essence_elements']
        with transaction.atomic():
            self.object = form.save()

            if essence_elements.is_valid():
                essence_elements.instance = self.object
                essence_elements.save()
        return super(EssenceCreateView, self).form_valid(form)


class EssenceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = 'essence/form.html'
    form_class = EssenceForm
    success_url = reverse_lazy('essence_index')

    def get_context_data(self, **kwargs):
        context = super(
            EssenceUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['essence_elements'] = EssenceElementFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['essence_elements'] = EssenceElementFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        essence_elements = context['essence_elements']
        with transaction.atomic():
            self.object = form.save()
            if essence_elements.is_valid():
                essence_elements.instance = self.object
                essence_elements.save()
        return super(EssenceUpdateView, self).form_valid(form)


class EssenceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Essence
    template_name = 'essence/delete.html'
    success_url = reverse_lazy('essence_index')

    def delete(self, request, *args, **kwargs):
        EssenceElement.objects.filter(essence_id=kwargs.get('pk')).delete()

        return super().delete(request, *args, **kwargs)
