from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from rareapi.models import RareUser

class UserView(ViewSet):
    def retrieve(self,request,pk):
      rare_user = RareUser.objects.get(pk = pk)
      serializer = UserSerializer(rare_user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list (self,request):
      rare_user = RareUser.objects.all()
      serializer = UserSerializer (rare_user,many= True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
      rare_user = RareUser.objects.get(pk=pk)
      uid = request.META["HTTP_AUTHORIZATION"]
      rare_user.first_name = request.data['firstName']
      rare_user.last_name = request.data['lastName']
      rare_user.bio = request.data['bio']
      rare_user.profile_image_url = request.data['profileImageUrl']
      rare_user.email = request.data['email']
      rare_user.uid = uid
      rare_user.save()
      
      return Response({'message': 'User Information has been Updated'}, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = RareUser
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on','active','is_staff', 'uid')
    depth = 1
    