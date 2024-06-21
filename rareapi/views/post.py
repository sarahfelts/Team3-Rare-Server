from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404

from rareapi.models import Post, Category, RareUser

class PostView(ViewSet):
    def retrieve(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST Operations for posts"""
        try:
            rare_user = get_object_or_404(RareUser, pk=request.data["rare_user"])
            category = get_object_or_404(Category, pk=request.data["category"])
            
            post = Post.objects.create(
                rare_user=rare_user,
                category=category,
                title=request.data["title"],
                publication_date=request.data["publication_date"],
                image_url=request.data["image_url"],
                content=request.data["content"],
                approved=request.data["approved"]
            )

            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        try:
            category = get_object_or_404(Category, pk=request.data['category'])
            rare_user = get_object_or_404(RareUser, pk=request.data['rare_user'])

            post.title = request.data['title']
            post.publication_date = request.data['publication_date']
            post.content = request.data['content']
            post.approved = request.data['approved']
            post.image_url = request.data['image_url']
            post.category = category
            post.rare_user = rare_user

            post.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        
        except KeyError as e:
            return Response({'error': f'Missing required field: {e}'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk): 
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved']
