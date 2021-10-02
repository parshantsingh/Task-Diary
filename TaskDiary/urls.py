from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from tasklist_app import views as tasklist_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasklist_app_views.index, name='index'),
    path('tasklist/', include('tasklist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact/', tasklist_app_views.contact, name='contact'),
    path('about/', tasklist_app_views.about, name='about'),
]
