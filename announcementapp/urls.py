from django.urls import path

from announcementapp.views import AnnouncementListView

app_name = 'announcementapp'

urlpatterns = [
    path('announcement_banner/', AnnouncementListView.as_view(), name='announcement_banner'),
]
