from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from rareapi.models import Post
from rareapi.models.category import Category
from rareapi.models.rare_user import RareUser

class PostView(ViewSet):
    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts=Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            category = Category.objects.get(pk=request.data['category'])
            rare_user = RareUser.objects.get(pk=request.data['rare_user'])
        except (Category.DoesNotExist, RareUser.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        post = Post.objects.create(
            rare_user=rare_user,
            category=category,
            title=request.data['title'],
            approved=request.data['approved'],
            publication_date=request.data['publication_date'],
            image_url=request.data['image_url'],
            content=request.data['content']
        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.title = request.data['title']
        post.publication_date = request.data['publication_date']
        post.content = request.data['content']
        post.approved = request.data['approved']
        post.image_url = request.data['image_url']

        try:
            category = Category.objects.get(pk=request.data['category'])
            rare_user = RareUser.objects.get(pk=request.data['rare_user'])
        except (Category.DoesNotExist, RareUser.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        post.category = category
        post.rare_user = rare_user
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk): 
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved']
