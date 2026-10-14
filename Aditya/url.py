from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .api import ProjectViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('Aditya/', views.Aditya, name='Aditya'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
