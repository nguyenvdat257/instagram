from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .my_imports import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    is_valid, error_fields = serializer.is_valid()
    if is_valid:
        serializer.save()
        return Response('Sign up successfully!')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def validate_user_signup(request):
    serializer = UserSerializer(data=request.data)
    is_valid, error_fields = serializer.is_valid()
    if is_valid:
        serializer.save()
        return Response('Sign up successfully!')
    else:
        return Response(error_fields, status=status.HTTP_400_BAD_REQUEST)

