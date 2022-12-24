from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UsersData
from .serializers import UserSerializer
# from rest_framework.decorators import api_view

class UserList(APIView):
    def get(self, request, pk=None):
        if pk:
            person=UsersData.objects.filter(id=pk)
            serializer = UserSerializer(person,many=True)
            return Response(serializer.data)
        else:
            person=UsersData.objects.all()
            serializer = UserSerializer(person,many=True)
            return Response(serializer.data)

    def put(self, request, pk):
        person = UsersData.objects.get(id=pk)
        serializer = UserSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)