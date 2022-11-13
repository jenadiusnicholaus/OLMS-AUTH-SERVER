from rest_framework import serializers
from django.db import models
from .Regions import RegionModel


class DistrictsModel(models.Model):
    region = models.ForeignKey(RegionModel, null=False, blank=False, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.region.region_name + '-' + self.district_name

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        db_table = 'tbl_districts'


class DistrictModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictsModel
        fields = '__all__'
