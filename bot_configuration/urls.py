from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'bot-configuration', BotGuildConfigurationViewSet)
router.register(r'discipline-sub', DisciplineSubConfigurationViewSet)
router.register(r'reaction-sub', ReactionSubConfigurationViewSet)

urlpatterns = router.urls
