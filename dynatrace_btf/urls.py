from django.conf.urls import url, include
from django.contrib import admin
import ln_alerts


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('ln_alerts.urls')),

]