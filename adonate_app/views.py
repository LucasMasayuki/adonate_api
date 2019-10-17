from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer

# Create your views here.
class UsersList(generics.ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer