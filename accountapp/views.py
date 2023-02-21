from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

has_ownership = [account_ownership_required, login_required] #데코레이터 하나로 정리


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('stateapp:create')
    template_name = 'accountapp/create.html'

@method_decorator(has_ownership, 'get') #함수랑 다르게 class에서는 decorator사용 불가하므로 변환 필요 로그인 필요
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class= AccountUpdateForm
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

