from django.shortcuts import render
from .models import *
from rest_framework import serializers
from .serializers import *
# from rest_framework.decorators import api_view   #for functions based view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView #for class based view 
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
# from rest_framework import generics  #for Generics Views
# from rest_framework import generics,mixins # for mixins view
#from rest_framework import viewsets

# # for function based view 

# # @api_view(['GET','POST'])

# # def task_view(request):

# #     if request.method=="GET":
# #         tasks=Task.objects.all()
# #         serializer=TaskSerializer(tasks,many=True)

# #         return Response(serializer.data)

# #     if request.method=="POST":
# #         data=request.data
# #         serializer=TaskSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)

# #         return Response(serializer.errors)

# # @api_view(['GET','PUT','DELETE'])

# # def task_details(request,pk):

# #     try:
# #         task=Task.objects.get(pk=pk)
# #     except Task.DoesNotExists:
# #         return Response(status=status.HTTP_404_NOT_FOUND)

# #     if request.method=="GET":
# #         serializer=TaskSerializer(task)
# #         return Response(serializer.data)

# #     if request.method=="PUT":
# #         data=request.data
# #         serializer=TaskSerializer(task,data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)

# #         return Response(serializer.errors)

# #     if request.method=="DELETE":
# #         task.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)



# # for class based view

class Taskview(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        responses={200: TaskSerializer(many=True)}
    )

    def get(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: TaskSerializer, 400: "Bad Request"}
    )


    def post(self,request):
        data=request.data
        serializer=TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class DetailTaskView(APIView):
    permission_classes = [AllowAny]

    def get_task(self,pk):
        task=Task.objects.get(pk=pk)
        return task


    @swagger_auto_schema(
        responses={200: TaskSerializer(), 404: 'Not Found'}
    )
    
    def get(self,request,pk):
        task=self.get_task(pk)
        serializer=TaskSerializer(task)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={200: TaskSerializer, 400: "Bad Request", 404: "Not Found"}
    )


    def put(self,request,pk):
        data=request.data
        task=self.get_task(pk)
        serializer=TaskSerializer(task,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )

    def delete(self,request,pk):
        task=self.get_task(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # this for generic view

# class TaskListCreate(generics.ListCreateAPIView):
#   queryset=Task.objects.all()
#   serializer_class= TaskSerializer


# class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#   queryset=Task.objects.all()
#   serializer_class=TaskSerializer



#  for Mixins view


# class TaskListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class TaskRetrieveUpdateDestroy(mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)


#     def delete(self,request,*args,**kwargs):
#         return self.delete(request,*args,**kwargs)


 # viewset

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset=Task.objects.all()
#     serializer_class=TaskSerializer











        






    



