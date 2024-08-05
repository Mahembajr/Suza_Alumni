# #from django.shortcuts import render

# # Create your views here.

# from rest_framework import viewsets
# from .models import AlumniProfile, JobPost, AlumniClub, Event, Reward
# from .serializers import AlumniProfileSerializer, JobPostSerializer, AlumniClubSerializer, EventSerializer, RewardSerializer

# class AlumniProfileViewSet(viewsets.ModelViewSet):
#     queryset = AlumniProfile.objects.all()
#     serializer_class = AlumniProfileSerializer

# class JobPostViewSet(viewsets.ModelViewSet):
#     queryset = JobPost.objects.all()
#     serializer_class = JobPostSerializer

# class AlumniClubViewSet(viewsets.ModelViewSet):
#     queryset = AlumniClub.objects.all()
#     serializer_class = AlumniClubSerializer

# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer

# class RewardViewSet(viewsets.ModelViewSet):
#     queryset = Reward.objects.all()
#     serializer_class = RewardSerializer


from rest_framework import viewsets
from .models import AlumniProfile, JobPost, AlumniClub, Event, Reward
from .serializers import AlumniProfileSerializer, JobPostSerializer, AlumniClubSerializer, EventSerializer, RewardSerializer

class AlumniProfileViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.all()
    serializer_class = AlumniProfileSerializer

    def list(self, request, *args, **kwargs):
        print("Fetching all alumni profiles")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("Creating a new alumni profile with data:", request.data)
        return super().create(request, *args, **kwargs)

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer

    def list(self, request, *args, **kwargs):
        print("Fetching all job posts")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("Creating a new job post with data:", request.data)
        return super().create(request, *args, **kwargs)

class AlumniClubViewSet(viewsets.ModelViewSet):
    queryset = AlumniClub.objects.all()
    serializer_class = AlumniClubSerializer

    def list(self, request, *args, **kwargs):
        print("Fetching all alumni clubs")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("Creating a new alumni club with data:", request.data)
        return super().create(request, *args, **kwargs)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        print("Fetching all events")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("Creating a new event with data:", request.data)
        return super().create(request, *args, **kwargs)

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    def list(self, request, *args, **kwargs):
        print("Fetching all rewards")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("Creating a new reward with data:", request.data)
        return super().create(request, *args, **kwargs)
