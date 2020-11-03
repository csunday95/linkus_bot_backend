
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import *


class TrackedReactionRoleEmbedCreateView(ModelViewSet):
    queryset = TrackedReactionRoleEmbed.objects.all()
    serializer_class = TrackedReactionRoleEmbedSerializer

    def _check_guild(self, request):
        embed = self.get_object()  # type: TrackedReactionRoleEmbed
        if 'guild_snowflake' not in request.query_params:
            return Response('Parameter "guild_snowflake" is required.', status=status.HTTP_400_BAD_REQUEST)
        # check that the requester is of the proper guild (not exactly secure, but its something)
        if str(embed.guild_snowflake) == request.query_params['guild_snowflake']:
            return None
        return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request: Request, *args, **kwargs):
        resp = self._check_guild(request)
        return super().retrieve(request, *args, **kwargs) if resp is None else resp

    def list(self, request, *args, **kwargs):
        if 'guild_snowflake' not in request.query_params:
            return Response('Parameter "guild_snowflake" is required.', status=status.HTTP_400_BAD_REQUEST)
        guild_snowflake = request.query_params['guild_snowflake']
        guild_embeds = TrackedReactionRoleEmbed.objects.filter(guild_snowflake=guild_snowflake)
        serializer = TrackedReactionRoleEmbedSerializer(instance=guild_embeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        resp = self._check_guild(request)
        return super().update(request, *args, **kwargs) if resp is None else resp

    def partial_update(self, request, *args, **kwargs):
        resp = self._check_guild(request)
        return super().partial_update(request, *args, **kwargs) if resp is None else resp

    def destroy(self, request, *args, **kwargs):
        resp = self._check_guild(request)
        return super().destroy(request, *args, **kwargs) if resp is None else resp

    @action(detail=True, methods=['post'])
    def add_mappings(self, request: Request, pk=None):
        resp = self._check_guild(request)
        if resp is not None:
            return resp
        embed = self.get_object()
        mapping_serializer = ReactionRoleEmojiMappingSerializer(data=request.data, many=True)
        if not mapping_serializer.is_valid():
            return Response(mapping_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for mapping in mapping_serializer.validated_data:
            mapping['tracked_embed'] = embed
            ReactionRoleEmojiMapping.objects.create(**mapping)
        return Response(status=status.HTTP_201_CREATED)
