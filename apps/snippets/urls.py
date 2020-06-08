from django.urls import path, include
from apps.snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets_options', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]
