from collections import Counter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import reverse, redirect
from django.views.generic import TemplateView, CreateView

from ragnarok.models import Simulator, SimulatorAttribute, \
    ResonanceRecipe, Resonance
from ragnarok.forms import SimulatorForm, SimulatorAttributeFormset


class SimulatorListView(TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'simulator/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resonances'] = Resonance.objects.filter(
            id__in=self.request.GET.getlist('resonance_ids')
        )

        return context


class SimulatorCreateView(CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Simulator
    template_name = 'simulator/form.html'
    form_class = SimulatorForm
    # success_url = reverse_lazy('simulator_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            SimulatorCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['simulator_attributes'] = SimulatorAttributeFormset(
                self.request.POST
            )
        else:
            context['simulator_attributes'] = SimulatorAttributeFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        simulator_attributes = context['simulator_attributes']
        # print(simulator_attributes)
        # print(self.object.name)
        self.object = form.save(commit=False)

        if not simulator_attributes.is_valid():
            return redirect(f"{reverse('simulator_create')}")

        simulator_attributes.instance = self.object
        monsters = [
            value for simulator_attribute in simulator_attributes.cleaned_data
            for key, value in simulator_attribute.items() if key == 'monster'
        ]
        essences = [
            value for simulator_attribute in simulator_attributes.cleaned_data
            for key, value in simulator_attribute.items() if key == 'essence'
        ]

        elements = []
        for monster in monsters:
            elements.extend(
                monster.elements.values_list('element', flat=True)
            )
        for essence in essences:
            elements.extend(
                essence.elements.values_list('element', flat=True)
            )
        elements_counter = Counter(elements)

        resonances = []
        for resonance in Resonance.objects.all():
            resonance_elements = resonance.resonancerecipe_set.all()
            match_recipes = []
            for resonance_element in resonance_elements:
                element_quantity = elements_counter.get(
                    resonance_element.element
                )
                if element_quantity and resonance_element.quantity <= element_quantity:
                    match_recipes.append(resonance_element)

            if len(resonance_elements) == len(match_recipes):
                resonances.append(resonance)

        if not resonances:
            return redirect(f"{reverse('simulator_create')}")

        query_string = ''
        for resonance in resonances:
            query_string += f'resonance_ids={resonance.id}&'

        return redirect(f"{reverse('simulator_index')}?{query_string}")
