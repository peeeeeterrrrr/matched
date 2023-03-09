from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView, ListView


from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountLoginForm, AccountCreateForm, AccountUpdateForm
from accountapp.models import CustomUser

has_ownership = [account_ownership_required, login_required]
class AccountLoginView(LoginView):
    form_class = AccountLoginForm
    template_name = 'accountapp/login.html'
    success_url = reverse_lazy('homescreens:homescreen')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(AccountLoginView, self).dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})



class AccountCreateView(CreateView):
    model = CustomUser
    form_class = AccountCreateForm

    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:login')
    def form_valid(self, form):
        temp_user= form.save(commit = False)
        temp_user.customuser = self.request.user
        temp_user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = CustomUser
    context_object_name = 'target_user'
    form_class= AccountUpdateForm
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = CustomUser
    context_object_name = 'target_user'
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

class AccountPasswordSearchView(View):
    model = CustomUser
    context_object_name = 'target_user'
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/password_search.html'

class AccountMenuView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'accountapp/accountmenu.html'



