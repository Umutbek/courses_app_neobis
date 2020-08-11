from django.test import TestCase

from core import models


class ModelTests(TestCase):
    def test_category_str(self):
        """Test the category string representation"""
        category = models.Category.objects.create(
            name='Programming',
            imgpath='path')
        self.assertEqual(str(category), category.name)

    def test_course_str(self):
        """Test the courses string representation"""
        course = models.Courses.objects.create(
            name='Python',
            description='Python is the best programming language',
            logo='SomeLogo',
            category=models.Category.objects.create(
                name='Programming',
                imgpath='path')
        )
        self.assertEqual(str(course), course.name)

    def test_branch_str(self):
        """Test the branch string representation"""
        branch = models.Branch.objects.create(
            latitude='12345',
            longitude='54321',
            address='Bishkek',
            course=models.Courses.objects.create(
                name='Python',
                description='Python is the best programming language',
                logo='SomeLogo',
                category=models.Category.objects.create(
                    name='Programming',
                    imgpath='path')
            )
        )
        self.assertEqual(str(branch), branch.address)

    def test_contact_str(self):
        """Test the contact string representation"""
        contact = models.Contact.objects.create(
            type=1,
            value='9963442324',
            course=models.Courses.objects.create(
                name='Python',
                description='Python is the best programming language',
                logo='SomeLogo',
                category=models.Category.objects.create(
                    name='Programming',
                    imgpath='path')
            )
        )
        self.assertEqual(str(contact), contact.value)
