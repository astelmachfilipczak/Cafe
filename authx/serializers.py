"""

"""

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

        extra_kwargs = {
            'password':{'write_only': True}
        } #hasła nie będzie widać w żądaniu

    def create(self, validated_data): #haszuje hasło
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
