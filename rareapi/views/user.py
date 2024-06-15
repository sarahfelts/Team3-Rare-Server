from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers,status
from rareapi.models import RareUser

class UserSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = RareUser
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on','active','is_staff', 'uid')
    depth = 1
    
class UserView(ViewSet):
    def retrieve(self,request,pk):
        user = RareUser.objects.get(pk = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list (self,request):
        users = RareUser.objects.all()
        serializer = UserSerializer (users,many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):

      user = RareUser.objects.get(pk=pk)
      uid = request.META["HTTP_AUTHORIZATION"]
      user.first_name = request.data['firstName']
      user.last_name = request.data['lastName']
      user.bio = request.data['bio']
      user.profile_image_url = request.data['profileImageUrl']
      user.email = request.data['email']
      user.uid = uid
      user.save()
      return Response({'message': 'User Information has been Updated'}, status=status.HTTP_204_NO_CONTENT)


        