from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rareapi.models import Post, Comment

class CommentView(viewsets.ViewSet):
    
    def list(self, request, post_id=None):
        queryset = Comment.objects.filter(post_id=post_id).order_by('-created_on')
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, post_id=None):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post, created_on=timezone.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, post_id=None):
        queryset = Comment.objects.filter(post_id=post_id)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk=None, post_id=None):
        queryset = Comment.objects.filter(post_id=post_id)
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, post_id=None):
        queryset = Comment.objects.filter(post_id=post_id)
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'subject', 'content', 'author', 'post', 'created_on']