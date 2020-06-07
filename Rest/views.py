from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from Rest import serializer
from rest_framework import viewsets
from Rest import models
from rest_framework.authentication import TokenAuthentication
from Rest import permissions
from rest_framework import filters
# Create your views here.

class Home(TemplateView):
	template_name = 'index.html'

class Api_view(APIView):
	""" list of api view """
	serializer_class = serializer.Serializer_view
	def get(self , request ,format=None):

		api_list = [ 'one ' , 'two ' , 'three']
		return Response({'key_no_one':'working on api view' , 'key_no_two':api_list})



	def post(self , request):
		"""  reterive serializers name view"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f' hello {name}'
			return Response({'serializer':message})
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



	def put(self , request , pk=None):
		""" update the whole content"""
		return Response({'put':'update whole content'})

	def delete(self , request , pk=None):
		""" delete the whole content"""
		return Response({'delete':'delete whole content'})

	def patch(self , request , pk=None):
		""" patch the sepecific  content"""
		return Response({'patch':'patch special content'})



class View_set(viewsets.ViewSet):

    serializer_class = serializer.Serializer_view
    def list(self, request):
        """ list of all object"""
        list_view =['one ' , 'two ' , 'three']
        return Response({'list_view':list_view})

    def create(self, request):
    	serializer= self.serializer_class(data=request.data)
    	if serializer.is_valid():
    		name = serializer.validated_data.get('name')
    		message = f'hell{name}'
    		return Response({'message':message})
    	else:
    		return Response(serializer.errors , status=HTTP_400_BAD_REQUEST)
    	 	
    def retrieve(self, request, pk=None):
        return Response({'retrieve':'retrieve_item'})


    def update(self, request, pk=None):
        return Response({'update':'user_item'})


    def partial_update(self, request, pk=None):
        return Response({'update_sepecified':'update sepecific item'})


    def destroy(self, request, pk=None):
        reuturn = Response({'delete':'delete item'})

			

class UserViewSet(viewsets.ModelViewSet):
	serializer_class = serializer.UserSerializer
	queryset = models.MyUser.objects.all()
	authentication_classes = [TokenAuthentication,]
	permission_classes =[permissions.UpdateOwnProfile,]
	filter_backends = [filters.SearchFilter]
	search_fields =['name','email']


     


