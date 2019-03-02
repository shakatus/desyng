from django.urls import path
from scales.viewset import PointViewSets, ScaleViewSets, RaiseViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('point',PointViewSets, base_name='point')
router.register('scale',ScaleViewSets, base_name='scale')
router.register('raise',RaiseViewSets, base_name='raise')
urlpatterns = []
urlpatterns += router.urls