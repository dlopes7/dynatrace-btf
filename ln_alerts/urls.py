from django.conf.urls import url

from ln_alerts import views

urlpatterns = [
    url(r'^$', views.bt_feed, name='bt_feed'),
]
