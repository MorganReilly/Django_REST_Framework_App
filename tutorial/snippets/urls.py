from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from snippets import views

# Including a schema for API
schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URLs are now determined automatically by the router
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
