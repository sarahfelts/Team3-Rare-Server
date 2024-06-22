from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag


class TagView(ViewSet):
    """Level up tags view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({'message': str(ex)}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all tags

        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all()

        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations to create a new tag

        Returns:
            Response -- JSON serialized tag instance
        """
        try:
            serializer = TagSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handle PUT requests to update a tag

        Returns:
            Response -- Empty body with 200 status code
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.label = request.data.get["label"]
            serializer = TagSerializer(tag, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except tag.DoesNotExist:
            return Response({'message': 'tag not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """Handle DELETE requests to delete a tag

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except tag.DoesNotExist:
            return Response({'message': 'tag not found'}, status=status.HTTP_404_NOT_FOUND)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""

    class Meta:
        model = Tag
        fields = ('id', 'label')
