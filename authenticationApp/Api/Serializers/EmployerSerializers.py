from rest_framework import serializers
from authenticationApp.Models import EmployerModels


class EmployerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerModels.EmployerModel
        fields = [
            'employer_name',
            'tin',
            'short_code',
            'employer_id'
        ]
