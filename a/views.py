from django.shortcuts import render
from .models import A
from .serializers import ASerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class AList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        a = A.objects.all()
        serializer = ASerializer(a, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ADetail(APIView):

    def get_object(self, pk):
        try:
            return A.objects.get(pk=pk)
        except A.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ASerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ASerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)