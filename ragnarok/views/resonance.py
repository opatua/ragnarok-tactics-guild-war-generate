from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ragnarok.models import Resonance, ResonaceRecipe
from ragnarok.forms import ResonanceForm, ResonaceRecipeFormset


class ResonanceDataView(BaseDatatableView):
    model = Resonance
    columns = [
        'name',
        'created_at',
        'updated_at',
        'manage',
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
                'resonance_update',
                kwargs={'pk': row.pk}
            )
            delete_link = reverse_lazy(
                'resonance_delete',
                kwargs={'pk': row.pk}
            )
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                update_link,
                delete_link
            )
            return manage
        else:
            return super(ResonanceDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class ResonanceListView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'resonance/index.html'


class ResonanceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Resonance
    template_name = 'resonance/form.html'
    form_class = ResonanceForm
    success_url = reverse_lazy('resonance_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            ResonanceCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['resonance_recipes'] = ResonaceRecipeFormset(
                self.request.POST
            )
        else:
            context['resonance_recipes'] = ResonaceRecipeFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ResonaceRecipes = context['resonance_recipes']
        with transaction.atomic():
            self.object = form.save()

            if ResonaceRecipes.is_valid():
                ResonaceRecipes.instance = self.object
                ResonaceRecipes.save()
        return super(ResonanceCreateView, self).form_valid(form)


class ResonanceUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Resonance
    template_name = 'resonance/form.html'
    form_class = ResonanceForm
    success_url = reverse_lazy('resonance_index')

    def get_context_data(self, **kwargs):
        context = super(
            ResonanceUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['resonance_recipes'] = ResonaceRecipeFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['resonance_recipes'] = ResonaceRecipeFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ResonaceRecipes = context['resonance_recipes']
        with transaction.atomic():
            self.object = form.save()
            if ResonaceRecipes.is_valid():
                ResonaceRecipes.instance = self.object
                ResonaceRecipes.save()
        return super(ResonanceUpdateView, self).form_valid(form)


class ResonanceDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Resonance
    template_name = 'resonance/delete.html'
    success_url = reverse_lazy('resonance_index')

    def delete(self, request, *args, **kwargs):
        ResonaceRecipe.objects.filter(resonance_id=kwargs.get('pk')).delete()

        return super().delete(request, *args, **kwargs)
