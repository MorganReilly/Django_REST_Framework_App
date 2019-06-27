from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.regiser(r'users', views.UserViewSet)

# API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]