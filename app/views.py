from django.shortcuts import render
from rest_framework.parsers import  JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics, authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.views import APIView
# Create your views here.

#
# @api_view(['GET','POST'])
# def studentview(request):
#     if request.method == "GET":
#         data = Student.objects.all()
#         serializer = StudentSerializer(data , many= True)
#         return JsonResponse(serializer.data ,safe= False)
#
#     elif request.method == "POST":
#
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors,status=400)
#
#
#     elif request.method == "DELETE":
#         data = Student.objects.get(id = id )
#         data.delete()



# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # permission_classes = [permissions.IsAuthenticated]


# class SnippetList(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#

class SnippetList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.name for user in Student.objects.all()]
        return Response(usernames)