import random, string
from django.shortcuts import render
from .serializers import TokenSerializer
from .models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TokenView(APIView):

	def get(self, request, format=None):
		magic_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(128))
		token = Token(payload=magic_string)
		token.save()
		return Response(TokenSerializer(token).data)