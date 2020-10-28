
from django.urls import path
from .views import *

urlpatterns = [
    path('tracked-reaction-embed/', TrackedReactionRoleEmbedCreateView.as_view()),
    path('tracked-reaction-embed/<int:message_snowflake>/', TrackedReactionRoleEmbedRetrieveView.as_view())
]
