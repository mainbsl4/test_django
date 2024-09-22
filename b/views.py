from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import B, A
from .serializers import BSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


# class BList(APIView):

#     def get(self, request, format=None):
#         b = B.objects.all()
#         serializer = BSerializer(b, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return B.objects.get(pk=pk)
#         except B.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class BList(APIView):
    """
    List all B objects, or create a new one.
    """
    def get(self, request, format=None):
        b = B.objects.all()
        serializer = BSerializer(b, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BSerializer(data=request.data)
        if serializer.is_valid():
            # Get related A object and decrement value by dic_value
            a_instance = get_object_or_404(A, pk=serializer.validated_data['a'].id)
            a_instance.value -= serializer.validated_data['dic_value']
            a_instance.save()

            # Save B instance
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BDetail(APIView):
    """
    Retrieve, update, or delete a B instance.
    """
    def get_object(self, pk):
        return get_object_or_404(B, pk=pk)

    def get(self, request, pk, format=None):
        # b_instance = self.get_object(pk)
        b_instance = B.objects.get(pk = pk)
        serializer = BSerializer(b_instance)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # b_instance = self.get_object(pk) 
        b_instance = B.objects.get(pk=pk) 
        old_dic_value = b_instance.dic_value  # Store old value

        serializer = BSerializer(b_instance, data=request.data)
        if serializer.is_valid():
            # Get related A object
            # a_instance = get_object_or_404(A, pk=serializer.validated_data['a'].id)
            a_instance = A.objects.get(pk=serializer.validated_data['a'].pk)

            # Adjust the A instance's value by the difference in dic_value
            a_instance.value += old_dic_value  # Undo the old dic_value
            a_instance.value -= serializer.validated_data['dic_value']  # Apply the new dic_value
            a_instance.save()

            # Save updated B instance
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        b_instance = B.objects.get(pk=pk)

        # Get related A object and increment value by dic_value (since B is being deleted)
        a_instance = b_instance.a
        a_instance.value += b_instance.dic_value
        a_instance.save()

        # Delete B instance
        b_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
