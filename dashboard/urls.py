from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.dashboardLogin, name='login'),
    url(r'^auth', views.dashboardAuth, name='auth'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^alerts', views.manageAlerts, name='alerts'),
    url(r'^alert_detail/(?P<uuid>[^/]+)/$', views.alertDetail, name='alert_details'),
    url(r'^students', views.manageStudents, name='students'),
    url(r'^students/(?P<student_id>[^/]+)/$', views.studentProfile, name='profile')
]
