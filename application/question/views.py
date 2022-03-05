from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
from .response import *

class QuestionViewsets(viewsets.ViewSet):

    def list(self, request):
        """API Endpoint for Question list"""
        if request.method == 'GET':
            question = Question.objects.all()
            if question is not None:
                serializer = QuestionSerializer(question, many=True)
                response = success_response(status.HTTP_200_OK, serializer.data)
                return Response(response)
            else:
                response = error_response(status.HTTP_400_BAD_REQUEST, serializer.errors)
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """API Endpoint for creating question"""
        if request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = success_response(status.HTTP_201_CREATED, serializer.data)
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = error_response(status.HTTP_400_BAD_REQUEST, serializer.errors)
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """API Endpoint for retrieving single question"""
        if request.method == 'GET':
            try:
                question = Question.objects.get(id=pk)
                serializer = QuestionSerializer(instance=question)
                response = success_response(status.HTTP_200_OK, serializer.data)
                return Response(response)
            except:
                response = error_response(status.HTTP_404_NOT_FOUND, "Question not found")
                return Response(response, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """API Endpoint for updating question"""
        if request.method == 'PUT':
            try:
                question = Question.objects.get(id=pk)
                serializer = QuestionSerializer(instance=question, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    response = success_response(status.HTTP_201_CREATED, serializer.data)
                    return Response(response, status=status.HTTP_201_CREATED)
                else:
                    response = error_response(status.HTTP_400_BAD_REQUEST, serializer.errors)
                    return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except:
                response = error_response(status.HTTP_404_NOT_FOUND, "Question not found")
                return Response(response, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        """API Endpoint for deleting question"""
        if request.method == 'DELETE': 
            try:
                question = Question.objects.get(id=pk)
                question.delete()
                response = delete_success_response(status.HTTP_200_OK, "Question data successfully deleted")
                return Response(response)
            except:
                response = error_response(status.HTTP_404_NOT_FOUND, "Question not found")
                return Response(response, status=status.HTTP_404_NOT_FOUND)
        else:
            response = error_response(status.HTTP_400_BAD_REQUEST, "Error deleting question data")
            return Response(response, status=status.HTTP_400_BAD_REQUEST)