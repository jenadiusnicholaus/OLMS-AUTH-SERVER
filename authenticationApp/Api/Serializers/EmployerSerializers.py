from rest_framework import serializers
from authenticationApp.Models import Employer


class EmployerLoginSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(many=False, read_only=True, slug_field='region_name')
    sector = serializers.SlugRelatedField(many=False, read_only=True, slug_field='sector_name')

    class Meta:
        model = Employer.EmployerModel
        fields = [
            'employer_name',
            'tin',
            'short_code',
            'employer_id',
            'region',
            'sector',
        ]
