from django.conf.urls import patterns, url
from directory import views

urlpatterns = patterns(
    '',
    url(r'^getdirectoryusers$', view=views.UserViewSet.as_view(), name='directoryusers'),
)
