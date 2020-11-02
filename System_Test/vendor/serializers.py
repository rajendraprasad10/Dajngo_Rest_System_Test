from rest_framework import serializers
from .models import VendorMdel
from django.contrib.auth import get_user_model

# ======================Vendor and Bidder  serializers -============================================================

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorMdel
        fields = "__all__"


# --------------------------- registration API  -------------------------

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorMdel
        fields = "['first_name', 'last_name', 'email', 'conform_email', 'password', 'conform_password']"
    def save(self):
        account = VendorMdel(
            first_name = self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        email = self.validated_data['email']
        conform_email = self.validated_data['conform_email']
        password = self.validated_data['password']
        conform_password = self.validated_data['conform_password']
        if email != conform_email:
            raise serializers.ValidationError({'email': 'Email must match'})
        account.set_email(email)
        account.save()

        if password != conform_password:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account




