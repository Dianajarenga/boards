
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user ,setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user=super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save()


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField(
        style={'input_type:password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username='email',
            password='password'

        )
        if not user:
            msg = _('unable to authenticate user')
            raise serializers.ValidationError(msg, code='authentication')
            attrs['user'] = user
            return attrs
