from django.urls import include, path

urlpatterns = [
    path('bro', include('apps.main.urls')),
    path('', include('apps.login.urls')),
]
