from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountUpdateView, AccountDeleteView, AccountCreateView, AccountLoginView

app_name = 'accountapp'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('create/', AccountCreateView.as_view(), name='create'),
]
