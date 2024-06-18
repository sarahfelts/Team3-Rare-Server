from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag, Post, Tag


class PostTagView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        try:
            post_tag = PostTag.objects.get(pk=pk)
            serializer = PostTagSerializer(post_tag)

            return Response(serializer.data)
        except PostTag.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """
        post_tags = PostTag.objects.all()

        tag_id = request.query_params.get('tag', None)
        if tag_id:
            post_tags = post_tags.filter(tag_id=tag_id)

        post_id = request.query_params.get('post', None)
        if post_id:
            song_posts = song_posts.filter(post_id=post_id)

        serializer = PostTagSerializer(post_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations to create a new PostTag

        Returns:
            Response -- JSON serialized PostTag instance
        """
        try:
            tag_id = request.data.get("tagId")
            post_id = request.data.get("postId")

            tag = Tag.objects.get(pk=tag_id)
            post = Post.objects.get(pk=post_id)

            post_tag = PostTag.objects.create(post=post, tag=tag)
            serializer = PostTagSerializer(post_tag)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handle PUT requests to update a PostTag

        Returns:
            Response -- Empty body with 200 status code
        """
        try:
            post_tag = PostTag.objects.get(pk=pk)
            post_id = request.data.get["postId"]
            tag_id = request.data.get["tagId"]

            post = Post.objects.get(pk=post_id)
            tag = Tag.objects.get(pk=tag_id)

            post_tag.tag = tag
            post_tag.post = post
            post_tag.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PostTag.DoesNotExist:
            return Response({'message': 'PostTag not found'}, status=status.HTTP_404_NOT_FOUND)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        except Tag.DoesNotExist:
            return Response({'message': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a PostTag

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            post_tag = PostTag.objects.get(pk=pk)
            post_tag.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except PostTag.DoesNotExist:
            return Response({'message': 'PostTag not found'}, status=status.HTTP_404_NOT_FOUND)


class PostTagSerializer(serializers.ModelSerializer):
    """JSON serializer for PostTags"""

    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PostTag
        fields = ('id', 'post_id', 'tag_id')
