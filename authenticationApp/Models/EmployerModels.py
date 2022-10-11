from django.db import models


class EmployerModel(models.Model):
    employer_id = models.IntegerField(null=False, blank=False, primary_key=True)
    employer_name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    tin = models.CharField(max_length=100, blank=False, null=False)
    short_code = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.employer_name

    class Meta:
        verbose_name = 'Employer',
        verbose_name_plural = 'Employers'
