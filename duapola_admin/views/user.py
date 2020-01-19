from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django_datatables_view.base_datatable_view import BaseDatatableView

from duapola_admin.forms import UserForm, UserProfileEditForm, UserPasswordChangeForm
from duapola_backend.models import User


class UserDataView(BaseDatatableView):
    model = User
    columns = [
        'email',
        'name',
        'is_active',
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
        elif column == 'manage':
            change_password_link = reverse_lazy(
                'user_password', kwargs={'pk': row.pk})
            update_link = reverse_lazy(
                'user_update', kwargs={'pk': row.pk})
            delete_link = reverse_lazy(
                'user_delete', kwargs={'pk': row.pk})
            manage = "<a href='{}' class='btn btn-info'><i class='fa fa-lock'></i></a>&nbsp;<a href='{}' class='btn btn-info'><i class='fa fa-pencil-alt'></i></a>&nbsp;<a href='{}' class='btn btn-danger'><i class='fa fa-trash'></i></a>".format(
                change_password_link, update_link, delete_link)
            return manage
        else:
            return super(UserDataView, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(email__icontains=search) |
                Q(name__icontains=search)
            )
        return qs


class UserListView(TemplateView):
    template_name = "user/index.html"


class UserCreateView(CreateView):
    model = User
    template_name = "user/create.html"
    form_class = UserForm
    success_url = reverse_lazy("user_index")


class UserUpdateView(UpdateView):
    model = User
    template_name = "user/update.html"
    form_class = UserProfileEditForm
    success_url = reverse_lazy("user_index")


class UserPasswordChangeView(UpdateView):
    model = User
    template_name = "user/change_password.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('user_index')

    def get_initial(self):
        initial = super(UserPasswordChangeView, self).get_initial()
        initial['password'] = ''
        return initial


class UserDeleteView(DeleteView):
    model = User
    template_name = "user/delete.html"
    success_url = reverse_lazy('user_index')
