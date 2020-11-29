
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tracked-reaction-embed', TrackedReactionRoleEmbedCreateView)

urlpatterns = router.urls
