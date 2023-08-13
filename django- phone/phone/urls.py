
from django.contrib import admin
from django.urls import path
from information_app.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
    path('phoneoffice/',home ),
    path('phoneoffice/fani',fani)
    path('phoneoffice/kar',kar ),
    path('phoneoffice/tamin',tamin ),
    path('phoneoffice/uni',uni ),
]
