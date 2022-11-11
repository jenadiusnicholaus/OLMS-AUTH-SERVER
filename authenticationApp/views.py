from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Permission
from .Models import UserCategory


# Create your views here.

def get_user_permissions(user):
    if user.is_superuser:
        return Permission.objects.all()
    return user.user_permissions.all() | Permission.objects.filter(group__user=user)


def get_user_category_and_object(user):
    user_category_obj = UserCategory.UserCategory.objects.filter(user=user)
    print(user_category_obj)
    sz = UserCategory.UserCategorySerializer(user_category_obj, many=True)
    return sz.data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims -- simply add things to the encrypted token
        # token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email
        user_category_data = get_user_category_and_object(user=self.user)
        permissions = get_user_permissions(user=self.user).values_list('codename', flat=True)
        user_groups = self.user.groups.all().values_list('name', flat=True)
        data['permissions'] = permissions
        data['groups'] = user_groups
        data['user_category'] = user_category_data
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
