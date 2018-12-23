import random, string
from django.shortcuts import render
from .serializers import TokenSerializer
from .models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TokenView(APIView):

	def get(self, request, format=None):
		magic_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(128))
		token = Token(payload=magic_string)
		token.save()
		return Response(TokenSerializer(token).data)

	def post(self, request, format=None):
		payload = request.data['payload']
		try:
			token = Token.objects.get(payload=payload)
			return Response(status=status.HTTP_200_OK)
		except Token.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)