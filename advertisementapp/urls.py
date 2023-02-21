from django.urls import path
from advertisementapp.views import AdvertisementListView

app_name = 'advertisementapp'

urlpatterns = [
    path('advertisementbanner/', AdvertisementListView.as_view(), name='advertisementbanner'),
]
