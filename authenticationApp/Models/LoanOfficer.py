from django.db import models
from rest_framework import serializers

LOAN_OFFICER_ROLE_CHOICES = (
    ('LO', 'HLI Loan Officer'),
    ('LAO', 'Loan Allocation Officer'),
    ('SLAO', 'Senior Loan Allocation Officer'),
    ('MLO', 'Manager Loan Allocation Officer'),
    ('ADLA', 'Assistant Director Loan Allocation'),
    ('ADLD', 'Assistant Director Loan Disbursement'),
    ('LDO', 'Loan Disbursement Officer'),
    ('SLDO', 'Senior Loan Disbursement Officer'),
    ('MLD', 'Manager Loan Disbursement'),
)

SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
);


class LoanOfficerModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=30, blank=False, choices=LOAN_OFFICER_ROLE_CHOICES)
    # role_id = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10)

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
