from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from Rest import serializer
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



			





