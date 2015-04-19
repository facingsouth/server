from rest_framework.routers import DefaultRouter
from events import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'followers', views.FollowerViewSet)