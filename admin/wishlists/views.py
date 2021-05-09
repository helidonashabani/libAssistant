from rest_framework import viewsets, status
from rest_framework.response import Response

# from .producer import publish
from .serializers import WishlistsSerializer


class WishlistsViewSet(viewsets.ViewSet):
    def list(self, request):
        return 'Hello'

    def create(self, request):
        serializer = WishlistsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
