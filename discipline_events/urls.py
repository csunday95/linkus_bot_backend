from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'discipline-type', UserDisciplineTypeViewSet)
router.register(r'discipline-event', UserDisciplineEventViewSet)

urlpatterns = router.urls
