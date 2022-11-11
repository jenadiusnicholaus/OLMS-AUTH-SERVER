from django.db import models
from rest_framework import serializers


class SectorsModel(models.Model):
    sector_id = models.IntegerField(blank=False, null=False, primary_key=True)
    sector_name = models.CharField(blank=False, null=False, unique=True, max_length=100)
    sector_description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.sector_name}'

    class Meta:
        verbose_name = 'Sector',
        verbose_name_plural = 'Sectors'
        db_table = 'tbl_employer_sectors'


class SectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorsModel
        fields = '__all__'
