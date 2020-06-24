import itertools
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from random import randint

from ragnarok.models import Character


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        characters = Character.objects.order_by('point')
        first_three_groups = self.chunks(characters, 3)
        character_groups = self.generate(
            self.chunks(first_three_groups[:-1], 5)
        ) + [first_three_groups[-1]]

        process_character_groups = []
        for character_group in character_groups:
            total_point = 0

            for character in character_group:
                total_point += character.point

            process_character_groups.append({
                'total_point': total_point,
                'average_point': round(total_point / len(character_group), 2),
                'character_group': character_group,
            })

        context['character_groups'] = process_character_groups

        return context

    def chunks(self, lst, N):
        return [lst[n:n+N] for n in range(0, len(lst), N)]

    def generate(self, list_):
        small = list(itertools.chain.from_iterable(list_[0]))
        big = list(itertools.chain.from_iterable(list_[1]))
        big.reverse()
        big = self.chunks(big, 2)

        small_iter = iter(small)
        new_group = []
        for big_set in big:
            big_set.append(next(small_iter))
            if len(big_set) == 2:
                big_set.append(next(small_iter))

            new_group.append(big_set)

        return self.chunks(list(small_iter), 3) + new_group
