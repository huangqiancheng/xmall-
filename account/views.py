from django.contrib.auth import get_user_model

# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import generics, viewsets

from account.serializers import UserSerializer, UserSerializerPassWdPost, UserPhotoUpload

User = get_user_model()
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username = username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except (User.DoesNotExist,User.MultipleObjectsReturned):
            return None
# class UserView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # authentication_classes = []
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             serializer_class = UserSerializer
#             return serializer_class
#         elif self.request.method == 'POST':
#             serializer_class =  UserSerializerPassWdPost
#             return serializer_class
#         else:
#             serializer_class = UserSerializer
#             return serializer_class
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "username"
    serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            serializer_class = UserSerializer
            return serializer_class
        elif self.action == 'create':
            serializer_class =  UserSerializerPassWdPost
            return serializer_class
        elif self.action == "partial_update":
            serializer_class = UserPhotoUpload
            return serializer_class
        else:
            serializer_class = UserSerializer
            return serializer_class

# class UserDetail(generics.RetrieveAPIView):
#     lookup_field ="username"
#     queryset = User.objects.all()
#     serializer_class = UserSerializer