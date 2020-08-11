from rest_framework import serializers
from core import models


class CategorySerializer(serializers.ModelSerializer):
    """Serialize Category part"""
    class Meta:
        model = models.Category
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    """Serialize Branch"""

    class Meta:
        model = models.Branch
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Serialize Contact"""

    class Meta:
        model = models.Contact
        fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    """Serialize Courses"""
    branches = BranchSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = models.Courses
        fields = ('id', 'name', 'description',
                  'category', 'logo', 'branches', 'contacts')

    def create(self, validated_data):
        branch = validated_data.pop('branches')
        contact = validated_data.pop('contacts')
        course = models.Courses.objects.create(**validated_data)
        for b in branch:
            models.Branch.objects.create(course=course, **b)
        for c in contact:
            models.Contact.objects.create(course=course, **c)
        return course
