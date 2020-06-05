from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Home(TemplateView):
	template_name = 'index.html'

class Api_view(APIView):
	""" list of api view """
	def get(self , request ,format=None):

		api_list = [ 'one ' , 'two ' , 'three']
		return Response({'key_no_one':'working on api view' , 'key_no_two':api_list})

