from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from core.models import Courses, Category

COURSES_URL = reverse('core:courses')


class ViewCourseApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name='Programming', imgpath='path')
        self.course = Courses.objects.create(
            name='Python',
            description='Python is the best programming language',
            logo='SomeLogo',
            category=self.category
        )

    def test_get_course(self):
        """Test retrieving courses"""

        res = self.client.get(COURSES_URL)

        self.assertEqual(res.status_code, 200)

    def test_post_course(self):
        """Test creating new course"""
        data = {
            'name': 'Math',
            'description': 'Math is everything',
            'logo': 'some text',
            'category': 1,
            'branches': [{
                        'latitude': '54335',
                        'longitude': '75635',
                        'address': 'Bishkek',
                        }],

            'contacts': [{
                        'type': 3,
                         'value': 'karimovumumtbek@gmail.com',
                         }]
        }

        res = self.client.post(COURSES_URL, data, format='json')
        self.assertEqual(res.status_code, 200)

    def test_get_by_id_course(self):
        """Test retrieving courses by id"""
        res = self.client.get(
            reverse('core:courses_id', kwargs={'pk': self.course.pk})
        )
        self.assertEqual(res.status_code, 200)

    def test_delete_course(self):
        """Test deleting course"""
        res = self.client.delete(
            reverse('core:courses_id', kwargs={'pk': self.course.pk}))
        self.assertEquals(res.status_code, 204)
