from rest_framework import routers
from .viewsets import RemisionViewSet, AcompananteViewSet

router = routers.SimpleRouter()
router.register('remisiones', RemisionViewSet)
router.register('acompanante', AcompananteViewSet)

urlpatterns = router.urls