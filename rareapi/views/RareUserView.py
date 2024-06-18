from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser

class RareUserView(ViewSet):
    """Rare API user view"""
    
    def list(self, request):
        """Handle GET requests to get all users """
        queryset = RareUser.objects.all()

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user """
        try:
            user = RareUser.objects.get(pk=pk)
            serializer = SingleUserSerializer(user, many=False)
            return Response(serializer.data)
        except RareUser.DoesNotExist:
            return Response({'message': 'User does not exist.'}, status=404)

    @classmethod
    def get_extra_actions(cls):
        return []

    def update(self, request, pk=None):
        """Handle PUT requests for a user

        Returns:
            Response -- Empty body with 204 status code
        """
        user = RareUser.objects.get(pk=pk)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.bio = request.data["bio"]
        user.profile_image_url = request.data["profile_image_url"]
        user.email = request.data["email"]
        user.created_on = request.data["created_on"]
        user.active = request.data["active"]
        user.is_staff = request.data["is_staff"]
        user.uid = request.data["uid"]
        user.save()

        return Response({}, status=204)
    def destroy(self, request, pk):
        try:
            user = RareUser.objects.get(pk=pk)
            user.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except RareUser.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for gamers
    """
    class Meta:
        model = RareUser
        fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid' )
        
class SingleUserSerializer(serializers.ModelSerializer):
    """JSON serializer for a single user
    """
    full_name = serializers.SerializerMethodField()
    user_profile_type = serializers.SerializerMethodField()

    class Meta:
        model = RareUser
        fields = ('full_name', 'profile_image_url', 'email', 'created_on', 'user_profile_type')

    def get_full_name(self, obj):
        """Combine first_name and last_name into full_name"""
        return f"{obj.first_name} {obj.last_name}"

    def get_user_profile_type(self, obj):
        """Return 'Staff' if is_staff is True, otherwise return 'User'"""
        return 'Staff' if obj.is_staff else 'User'