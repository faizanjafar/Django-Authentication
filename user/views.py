from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserAccount
from .serializers import UserAccountSerializer
from django.db import IntegrityError


# Create your views here.
class RegisterUserView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return response
        except IntegrityError as e:
            return Response(
                {"error": "Email address must be unique."},
                status=status.HTTP_400_BAD_REQUEST,
            )
