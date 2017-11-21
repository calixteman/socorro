from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',
        views.index,
        name='index'),
    url(r'^crontabber/$',
        views.crontabber_status,
        name='crontabber_status'),
    url(r'^healthcheck/$',
        views.healthcheck,
        name='healthcheck'),
]
