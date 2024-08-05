#from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import AlumniProfile, JobPost, AlumniClub, Event, Reward

class AlumniProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.alumni_profile = AlumniProfile.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            professional_details='Software Engineer',
            education_history='BS in Computer Science',
            achievements='Created an awesome project'
        )

    def test_get_alumni_profiles(self):
        response = self.client.get('/api/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_alumni_profile(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com',
            'professional_details': 'Data Scientist',
            'education_history': 'MS in Data Science',
            'achievements': 'Published several papers'
        }
        response = self.client.post('/api/profiles/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class JobPostTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        self.alumni_profile = AlumniProfile.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            professional_details='Software Engineer',
            education_history='BS in Computer Science',
            achievements='Created an awesome project'
        )

        self.job_post = JobPost.objects.create(
            title='Backend Developer',
            description='Develop backend services',
            posted_by=self.alumni_profile
        )

    def test_get_job_posts(self):
        response = self.client.get('/api/jobs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_job_post(self):
        data = {
            'title': 'Frontend Developer',
            'description': 'Develop frontend applications',
            'posted_by': self.alumni_profile.id
        }
        response = self.client.post('/api/jobs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# More test cases for AlumniClub, Event, Reward models
