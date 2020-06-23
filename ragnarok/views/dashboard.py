import itertools

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from random import randint


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = [randint(2000, 5000) for count in range(0, 33)]
        data.sort()
        context['user'] = self.generate(self.chunks(self.chunks(data, 3), 5))

        return context

    def chunks(self, lst, N):
        return [lst[n:n+N] for n in range(0, len(lst), N)]

    def generate(self, list_):
        small = list(itertools.chain.from_iterable(list_[0]))
        big = self.chunks(
            list(
                itertools.chain.from_iterable(list_[1][:-1])
            ),
            2
        )
        small_iter = iter(small)
        new_group = []
        for big_set in big:
            big_set.append(next(small_iter))
            new_group.append(big_set)

        return self.chunks(list(small_iter), 3) + new_group
