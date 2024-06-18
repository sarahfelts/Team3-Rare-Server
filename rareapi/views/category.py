from rest_framework import  status, serializers
from rest_framework.response import Response
from rareapi.models import Category
from rest_framework.viewsets import ViewSet



class CategoryView(ViewSet):
    
    def list(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many= True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def retrieve(self,request,pk):
         category = Category.objects.get(pk = pk)
         serializer = CategorySerializer(category)
         return Response(serializer.data, status=status.HTTP_200_OK)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['label']
        depth = 1