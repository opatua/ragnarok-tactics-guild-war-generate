import itertools
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from random import randint

from ragnarok.models import Team


class GuildWarSuggestionView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = "guild_war/sugesstion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teams = Team.objects.prefetch_related('character').order_by('point')
        first_three_groups = self._chunks(teams, 3)
        team_groups = self._generate(
            self._chunks(first_three_groups[:-1], 5)
        ) + [first_three_groups[-1]]

        process_team_groups = []
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
        small = list(itertools.chain.from_iterable(list_[0]))
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
