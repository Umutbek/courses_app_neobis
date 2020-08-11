from django.db import models


class Category(models.Model):
    """models for Category"""
    name = models.CharField(max_length=200)
    imgpath = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Courses(models.Model):
    """models for Course"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    """models for branch"""
    latitude = models.CharField(max_length=200, default=None)
    longitude = models.CharField(max_length=200, default=None)
    address = models.CharField(max_length=200, default=None)
    course = models.ForeignKey(Courses, related_name='branches',
                               on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    """models for contact"""
    phone = 1
    facebook = 2
    email = 3

    CONTACT_CHOICES = [
        (phone, 'Phone'),
        (facebook, 'Facebook'),
        (email, 'Email'),
    ]
    type = models.IntegerField(choices=CONTACT_CHOICES, default=None)
    value = models.CharField(max_length=200, default=None)
    course = models.ForeignKey(Courses, related_name='contacts', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.value
