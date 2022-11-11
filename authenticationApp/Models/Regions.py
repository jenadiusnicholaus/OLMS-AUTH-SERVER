from django.db import models


class RegionModel(models.Model):
    region_id = models.IntegerField(null=False, blank=False, primary_key=True)
    region_name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.region_name}'

    class Meta:
        verbose_name = 'Region',
        verbose_name_plural = 'Regions'
        db_table = 'tbl_regions'
