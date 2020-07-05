from collections import Counter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import reverse, redirect
from django.views.generic import TemplateView, CreateView

from ragnarok.models import Simulator, SimulatorAttribute, \
    ResonanceRecipe, Resonance, FactionBoost, FactionBoostAttribute
from ragnarok.forms import SimulatorForm, SimulatorAttributeFormset


class SimulatorBaseListView(TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resonances'] = Resonance.objects.filter(
            id__in=self.request.GET.getlist('resonance_ids')
        )
        context['faction_boosts'] = FactionBoost.objects.filter(
            id__in=self.request.GET.getlist('faction_boost_ids')
        )
        context['elements_counter'] = self.request.GET.get('elements_counter')
        context['factions_counter'] = self.request.GET.get('factions_counter')

        return context


class SimulatorListView(SimulatorBaseListView):
    def get_template_names(self):
        return ['simulator/index.html']


class SimulatorAdminListView(LoginRequiredMixin, SimulatorBaseListView):
    def get_template_names(self):
        return ['simulator/index_admin.html']


class SimulatorBaseCreateView(CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Simulator
    form_class = SimulatorForm

    def get_context_data(self, *args, **kwargs):
        context = super(
            SimulatorBaseCreateView,
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
        factions = []
        for monster in monsters:
            elements.extend(
                monster.elements.values_list('element', flat=True)
            )
            factions.append(monster.faction)
        for essence in essences:
            elements.extend(
                essence.elements.values_list('element', flat=True)
            )
        elements_counter = Counter(elements)
        factions_counter = Counter(factions)

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

        faction_boosts = []
        for faction_boost in FactionBoost.objects.all():
            faction_boost_attributes = faction_boost.factionboostattribute_set.all()
            match_attributes = []
            for faction_boost_attribute in faction_boost_attributes:
                faction_quantity = factions_counter.get(
                    faction_boost_attribute.faction
                )
                if faction_quantity and faction_boost_attribute.quantity <= faction_quantity:
                    match_attributes.append(faction_boost_attribute)

            if len(faction_boost_attributes) == len(match_attributes):
                faction_boosts.append(faction_boost)

        query_string = ''
        for resonance in resonances:
            query_string += f'resonance_ids={resonance.id}&'

        for faction_boost in faction_boosts:
            query_string += f'faction_boost_ids={faction_boost.id}&'

        redirect_url = reverse('simulator_admin_index') if getattr(self.request.user, 'id', None) \
            else reverse('simulator_index')

        return redirect(
            f"{redirect_url}?{query_string}&elements_counter={dict(elements_counter)}&factions_counter={dict(factions_counter)}"
        )


class SimulatorCreateView(SimulatorBaseCreateView):
    def get_template_names(self):
        return ['simulator/form.html']


class SimulatorAdminCreateView(LoginRequiredMixin, SimulatorBaseCreateView):
    def get_template_names(self):
        return ['simulator/form_admin.html']
