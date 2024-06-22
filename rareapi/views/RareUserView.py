from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, ValidationError
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
        if not isinstance(request.data, dict):
            return Response({'message': 'Invalid data format. Expected a JSON object.'}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            user = RareUser.objects.get(pk=pk)
        except RareUser.DoesNotExist:
            return Response({'message': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
        user.first_name = request.data.get("first_name", user.first_name)
        user.last_name = request.data.get("last_name", user.last_name)
        user.bio = request.data.get("bio", user.bio)
        user.profile_image_url = request.data.get("profile_image_url", user.profile_image_url)
        user.username = request.data.get("username", user.username)
        user.email = request.data.get("email", user.email)
        user.created_on = request.data.get("created_on", user.created_on)
        user.active = request.data.get("active", user.active)
        user.is_staff = request.data.get("is_staff", user.is_staff)
        user.uid = request.data.get("uid", user.uid)
        user.save()
    
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['put'], url_path='update_active_user')
    def update_active_user(self, request, pk=None):
        try:
            user = RareUser.objects.get(pk=pk)
        except RareUser.DoesNotExist:
            raise NotFound('User not found')
    
        active = request.data.get('active')
        if active is None:
            raise ValidationError('Missing "active" field in request data')
    
        user.active = active
        user.save()
    
        return Response({'status': 'active status updated'}, status=status.HTTP_200_OK)
    
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
        fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid', 'username')

        
class SingleUserSerializer(serializers.ModelSerializer):
    """JSON serializer for a single user
    """
    full_name = serializers.SerializerMethodField()
    user_profile_type = serializers.SerializerMethodField()
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = RareUser
        fields = ('full_name', 'profile_image_url', 'email', 'created_on', 'user_profile_type', 'display_name', 'username')

    def get_full_name(self, obj):
        """Combine first_name and last_name into full_name"""
        return f"{obj.first_name} {obj.last_name}"
    

    def get_user_profile_type(self, obj):
        """Return 'Staff' if is_staff is True, otherwise return 'User'"""
        return 'Staff' if obj.is_staff else 'User'
    
    def get_display_name(self, obj):
        """Get display name (username) for user"""
        return f"{obj.username}"