from django.urls import path

from homescreenapp.views import HomeScreenView, TeacherEmployeeView, AboutUsView, ContactView, UserGuideView

app_name = 'homescreenapp'

urlpatterns = [
    path('homescreen/',HomeScreenView.as_view(), name='homescreen'),
    path('userguide/',UserGuideView.as_view(), name='userguide'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('aboutus/',AboutUsView.as_view(), name='aboutus'),
    path('teacheremployee/',TeacherEmployeeView.as_view(), name='teacheremployee'),
]
