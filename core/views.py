from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core import serializers
from core import models


class CategoryView(APIView):
    """API view for category list"""
    serializer_class = serializers.CategorySerializer

    def get(self, request):
        """Return list of category"""
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response({"Categories": serializer.data})

    def post(self, request):
        """Create new category"""
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"Category '{}' created successfully".format(saved_data.name)})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """API view for category detail"""
    serializer_class = serializers.CategorySerializer

    def get(self, request, pk):
        """Return a list of category details"""
        category = models.Category.objects.get(pk=pk)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        """Handling updated object"""
        category = models.Category.objects.get(pk=pk)
        serializer = serializers.CategorySerializer(category,
                                                    data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting category"""
        category = models.Category.objects.get(pk=pk)
        category.delete()
        return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class BranchView(APIView):
    """API view for branch list"""
    serializer_class = serializers.BranchSerializer

    def get(self, request):
        """Return list of branch"""
        branch = models.Branch.objects.all()
        serializer = serializers.BranchSerializer(branch, many=True)
        return Response({"Branch": serializer.data})

    def post(self, request):
        """Create new branch"""
        serializer = serializers.BranchSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"Branch '{}' created successfully".format(saved_data.address)})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class BranchDetail(APIView):
    """API view for Branch detail"""
    serializer_class = serializers.BranchSerializer

    def get(self, request, pk):
        """Return a list of branch details"""
        branch = models.Branch.objects.get(pk=pk)
        serializer = serializers.BranchSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk):
        """Handling updated object"""
        branch = models.Branch.objects.get(pk=pk)
        serializer = serializers.BranchSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting branch"""
        branch = models.Branch.objects.get(pk=pk)
        branch.delete()
        return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class ContactView(APIView):
    """API view for contact list"""
    serializer_class = serializers.ContactSerializer

    def get(self, request):
        """get category data"""
        contact = models.Contact.objects.all()
        serializer = serializers.ContactSerializer(contact, many=True)
        return Response({"Contact": serializer.data})

    def post(self, request):
        """Create new contact"""
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"Contact '{}' created successfully".format(saved_data.value)})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    """API view for contact details"""
    serializer_class = serializers.ContactSerializer

    def get(self, request, pk):
        """Return a list of contact details"""
        contact = models.Contact.objects.get(pk=pk)
        serializer = serializers.ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk):
        """Handling updated object"""
        contact = models.Contact.objects.get(pk=pk)
        serializer = serializers.ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting contact"""
        contact = models.Contact.objects.get(pk=pk)
        contact.delete()
        return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class CourseView(APIView):
    """API view for Course list"""
    serializer_class = serializers.CoursesSerializer

    def get(self, request):
        """Return list of Course"""
        course = models.Courses.objects.all()
        serializer = serializers.CoursesSerializer(course, many=True)
        return Response({"Courses": serializer.data})

    def post(self, request):
        """Create new course"""
        serializer = serializers.CoursesSerializer(data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response({"Course '{}' created successfully".format(saved_data.name)})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    """API view for course details"""
    serializer_class = serializers.CoursesSerializer

    def get(self, request, pk):
        """Return list of course details"""
        course = models.Courses.objects.get(pk=pk)
        serializer = serializers.CoursesSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        """Handling updated object"""
        course = models.Courses.objects.get(pk=pk)
        serializer = serializers.CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting course object"""
        course = models.Courses.objects.get(pk=pk)
        course.delete()
        return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
