from rest_framework import serializers

from .models import Wishlists


class WishlistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlists
        fields = '__all__'