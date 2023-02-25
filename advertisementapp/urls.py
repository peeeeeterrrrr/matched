from django.urls import path
from advertisementapp.views import AdvertisementListView

app_name = 'advertisementapp'

urlpatterns = [
    path('advertisement_banner/', AdvertisementListView.as_view(), name='advertisement_banner'),
]
