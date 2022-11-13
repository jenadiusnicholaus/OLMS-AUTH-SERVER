from django.db import models
from rest_framework import serializers


class LoanOfficerModel(models.Model):
    officer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role_id = models.IntegerField()
    sex = models.CharField(max_length=1)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.last_name}, {self.first_name} {self.first_name})'

    class Meta:
        verbose_name = 'LoanOfficer',
        verbose_name_plural = 'LoanOfficers'
        db_table = 'tbl_loan_officers'


class LoanOfficerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanOfficerModel
        fields = '__all__'
