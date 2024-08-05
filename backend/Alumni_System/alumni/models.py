#from django.db import models

# Create your models here.
from django.db import models

class AlumniProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    professional_details = models.TextField()
    education_history = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(AlumniProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AlumniClub(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    members = models.ManyToManyField(AlumniProfile)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey(AlumniProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reward(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    awarded_to = models.ForeignKey(AlumniProfile, on_delete=models.CASCADE)
    date_awarded = models.DateTimeField()

    def __str__(self):
        return self.name
