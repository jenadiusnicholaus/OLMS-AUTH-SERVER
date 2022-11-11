from django.db import models
from .Regions import RegionModel
from .Sectors import SectorsModel

EMPLOYER_CATEGORY_CHOICES = (
    (1, 'PUBLIC EMPLOYERS'),
    (2, 'CENTRAL GOVERMENT EMPLOYERS'),
    (3, 'PRIVATE EMPLOYERS')
)


class EmployerModel(models.Model):
    employer_id = models.IntegerField(null=False, blank=False, primary_key=True)
    employer_name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    tin = models.CharField(max_length=100, blank=False, null=False)
    short_code = models.CharField(max_length=20, null=False, blank=False)
    postal_address = models.CharField(max_length=100, null=True, blank=True)
    physical_address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact_person_name = models.CharField(max_length=100, null=True, blank=True)
    contact_person_position = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile = models.CharField(max_length=100, null=True, blank=True)
    contact_person_telephone = models.CharField(max_length=100, null=True, blank=True)
    contact_person_email = models.CharField(max_length=100, null=True, blank=True)
    vote_code = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    control_number = models.BigIntegerField(null=True, blank=True)
    vote_no = models.CharField(max_length=100, null=True, blank=True)
    region = models.ForeignKey(RegionModel, null=False, blank=False, on_delete=models.RESTRICT)
    sectors = models.ForeignKey(SectorsModel, null=False, blank=False, on_delete=models.RESTRICT)
    category = models.IntegerField(null=False, blank=False, default=3, choices=EMPLOYER_CATEGORY_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.employer_name

    class Meta:
        verbose_name = 'Employer',
        verbose_name_plural = 'Employers'
