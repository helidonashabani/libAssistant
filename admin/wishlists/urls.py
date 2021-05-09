from django.urls import path

from .views import WishlistsViewSet

urlpatterns = [
    path('wishlists', WishlistsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }))
]