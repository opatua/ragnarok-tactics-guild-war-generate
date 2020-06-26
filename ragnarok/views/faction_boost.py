from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import FactionBoost, FactionBoostAttribute
from ragnarok.forms import FactionBoostForm, FactionBoostAttributeFormset


class FactionBoostDataView(BaseDatatableView):
    model = FactionBoost
    columns = [
        'name',
        'manage',
    ]

    def render_column(self, row, column):
        if column == 'manage':
            update_link = reverse_lazy(
                'faction_boost_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'faction_boost_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(FactionBoostDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class FactionBoostListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'faction_boost/index.html'


class FactionBoostCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = FactionBoost
    template_name = 'faction_boost/form.html'
    form_class = FactionBoostForm
    success_url = reverse_lazy('faction_boost_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            FactionBoostCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['faction_boost_attributes'] = FactionBoostAttributeFormset(
                self.request.POST
            )
        else:
            context['faction_boost_attributes'] = FactionBoostAttributeFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        faction_boost_attributes = context['faction_boost_attributes']
        with transaction.atomic():
            self.object = form.save()

            if faction_boost_attributes.is_valid():
                faction_boost_attributes.instance = self.object
                faction_boost_attributes.save()
        return super(FactionBoostCreateView, self).form_valid(form)


class FactionBoostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = FactionBoost
    template_name = 'faction_boost/form.html'
    form_class = FactionBoostForm
    success_url = reverse_lazy('faction_boost_index')

    def get_context_data(self, **kwargs):
        context = super(
            FactionBoostUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['faction_boost_attributes'] = FactionBoostAttributeFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['faction_boost_attributes'] = FactionBoostAttributeFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        faction_boost_attributes = context['faction_boost_attributes']
        with transaction.atomic():
            self.object = form.save()
            if faction_boost_attributes.is_valid():
                faction_boost_attributes.instance = self.object
                faction_boost_attributes.save()
        return super(FactionBoostUpdateView, self).form_valid(form)


class FactionBoostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = FactionBoost
    template_name = 'faction_boost/delete.html'
    success_url = reverse_lazy('faction_boost_index')

    def delete(self, request, *args, **kwargs):
        FactionBoostAttribute.objects.filter(
            faction_boost_id=kwargs.get('pk')
        ).delete()

        return super().delete(request, *args, **kwargs)
