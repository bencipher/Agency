from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('solve', views.home, name="home"),
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('mission', views.mission, name="add"),
    path('about', views.about, name="add"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)