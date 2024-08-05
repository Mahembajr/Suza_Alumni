from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumniProfileViewSet, JobPostViewSet, AlumniClubViewSet, EventViewSet, RewardViewSet

router = DefaultRouter()
router.register(r'profiles', AlumniProfileViewSet)
router.register(r'jobs', JobPostViewSet)
router.register(r'clubs', AlumniClubViewSet)
router.register(r'events', EventViewSet)
router.register(r'rewards', RewardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
