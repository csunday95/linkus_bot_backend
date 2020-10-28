
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.mixins import RetrieveModelMixin
from .models import *
from .serializers import *


class TrackedReactionRoleEmbedCreateView(generics.ListCreateAPIView, RetrieveModelMixin):
    queryset = TrackedReactionRoleEmbed
    serializer_class = TrackedReactionRoleEmbedSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        embed_serializer = TrackedReactionRoleEmbedSerializer(data=request.data, many=False)
        if embed_serializer.is_valid():
            created_instance = embed_serializer.save()
            result_serializer = TrackedReactionRoleEmbedSerializer(instance=created_instance)
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(embed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackedReactionRoleEmbedRetrieveView(generics.RetrieveAPIView):
    queryset = TrackedReactionRoleEmbed
    serializer_class = TrackedReactionRoleEmbedSerializer
    lookup_field = 'message_snowflake'
