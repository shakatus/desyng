from django.urls import path
from scales.viewset import PointViewSets, ScaleViewSets, RaiseViewSets
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = DefaultRouter()
router.register('point',PointViewSets, base_name='point')
router.register('scale',ScaleViewSets, base_name='scale')
router.register('raise',RaiseViewSets, base_name='raise')
#scales_router = routers.NestedSimpleRouter(router,r'scales',lookup='scale')
#scales_router.register(r'raises', RaiseViewSet, base_name='scale-raise')

urlpatterns = [
	path('bascula/<int:point_id>/',views.results)
]
urlpatterns += router.urls
#urlpatterns = patterns('',
#    url(r'^', include(router.urls)),
#    url(r'^', include(scales_router.urls)),
#)
