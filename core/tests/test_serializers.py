from django.test import TestCase

from core import serializers, models


class SerializerTesting(TestCase):
    """Test serializer"""
    def setUp(self):
        self.course = models.Courses.objects.create(
            name='Python',
            description='Python is the best programming language',
            logo='SomeLogo',
            category=models.Category.objects.create(
                name='Programming',
                imgpath='path')
        )
        self.serializer = serializers.CoursesSerializer(instance=self.course)

    def test_fields(self):
        """Test expected field"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'category', 'logo', 'branches', 'contacts']))

    def test_name_field(self):
        """Test course name field content"""
        data = self.serializer.data
        self.assertEqual(data['name'], self.course.name)

    def test_description_field(self):
        """Test course description field content"""
        data = self.serializer.data
        self.assertEqual(data['description'], self.course.description)

    def test_logo_field(self):
        """Test course logo field content"""
        data = self.serializer.data
        self.assertEqual(data['logo'], self.course.logo)

    def test_existence(self):
        """Test existence"""
        exists = models.Courses.objects.get(id=1)
        self.assertIsNotNone(exists)
