from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'groups','user_permissions']
    
