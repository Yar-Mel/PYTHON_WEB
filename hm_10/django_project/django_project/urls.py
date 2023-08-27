from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("quotes_app.urls")),
    path('', include("users_app.urls")),
]
