import itertools
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from random import randint

from ragnarok.forms import CharacterForm, TeamFormset
from ragnarok.models import Character, Team


class GuildWarSuggestionView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = "guild_war/sugesstion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        process_team_groups = []
        teams = Team.objects.prefetch_related('character').order_by('point')
        if not teams:
            context['team_groups'] = process_team_groups

            return context

        first_three_groups = self._chunks(teams, 3)
        team_groups = self._generate(
            self._chunks(first_three_groups[:-1], 5)
        ) + [first_three_groups[-1]]

        for team_group in team_groups:
            total_point = 0

            for team in team_group:
                total_point += team.point

            process_team_groups.append({
                'total_point': total_point,
                'average_point': round(total_point / len(team_group), 2),
                'team_group': team_group,
            })

        context['team_groups'] = process_team_groups

        return context

    def _chunks(self, lst, N):
        return [lst[n:n+N] for n in range(0, len(lst), N)]

    def _generate(self, list_):
        if not list_:
            return []
        small = list(itertools.chain.from_iterable(list_[0]))
        if len(list_) < 2:
            return self._chunks(small, 3)
        big = list(itertools.chain.from_iterable(list_[1]))
        big.reverse()
        big = self._chunks(big, 2)

        small_iter = iter(small)
        new_group = []
        for big_set in big:
            big_set.append(next(small_iter))
            if len(big_set) == 2:
                big_set.append(next(small_iter))

            new_group.append(big_set)

        return self._chunks(list(small_iter), 3) + new_group


class GuildWarCharacterListView(TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'guild_war/index.html'


class GuildWarCharacterDataView(BaseDatatableView):
    model = Character
    columns = [
        'name',
        'updated_at',
        'manage',
    ]

    def render_column(self, row, column):
        if column == 'manage':
            update_link = reverse_lazy(
                'guild_war_character_update',
                kwargs={'pk': row.pk}
            )
            manage = f"<a href='{update_link}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp"

            return manage
        else:
            return super(GuildWarCharacterDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__icontains=search)
            )
        return qs


class GuildWarCharacterCreateView(CreateView):
    model = Character
    template_name = 'guild_war/form.html'
    form_class = CharacterForm
    success_url = reverse_lazy('guild_war_character_index')

    def get_context_data(self, *args, **kwargs):
        context = super(
            GuildWarCharacterCreateView,
            self
        ).get_context_data(*args, **kwargs)
        context['title'] = 'Create'
        if self.request.POST:
            context['teams'] = TeamFormset(
                self.request.POST
            )
        else:
            context['teams'] = TeamFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        teams = context['teams']
        with transaction.atomic():
            self.object = form.save()

            if teams.is_valid():
                teams.instance = self.object
                teams.save()
        return super(GuildWarCharacterCreateView, self).form_valid(form)


class GuildWarCharacterUpdateView(UpdateView):
    model = Character
    template_name = 'guild_war/form.html'
    form_class = CharacterForm
    success_url = reverse_lazy('guild_war_character_index')

    def get_context_data(self, **kwargs):
        context = super(
            GuildWarCharacterUpdateView,
            self
        ).get_context_data(**kwargs)
        context['title'] = 'Update - {}'.format(self.object.name)
        if self.request.POST:
            context['teams'] = TeamFormset(
                self.request.POST,
                instance=self.object
            )
        else:
            context['teams'] = TeamFormset(
                instance=self.object
            )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        teams = context['teams']
        with transaction.atomic():
            self.object = form.save()
            if teams.is_valid():
                teams.instance = self.object
                teams.save()
        return super(GuildWarCharacterUpdateView, self).form_valid(form)
