from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountLoginForm, AccountCreateForm, AccountUpdateForm
from accountapp.models import CustomUser

has_ownership = [account_ownership_required, login_required]

# createview에서는 form valid필수 get_success_url은 필수 x 웬만하면 reverse_lazy 로그인 필요하면 decorator
class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    template_name = 'accountapp/login.html'


class AccountCreateView(CreateView):
    model = CustomUser
    form_class = AccountCreateForm
    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:login')
    def form_valid(self, form):
        temp_user= form.save(commit=False)
        temp_user.writer =self.request.user
        temp_user.save()
        return super().form_valid(form)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = CustomUser
    context_object_name = 'target_user'
    form_class= AccountUpdateForm
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = CustomUser
    context_object_name = 'target_user'
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

