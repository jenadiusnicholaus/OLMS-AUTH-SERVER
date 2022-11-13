from django.db import models
from django.utils.translation import gettext as _

from .Employer import EmployerModel, EmployerModelSerializer
from .Beneficiary import BeneficiaryModel, BeneficiaryModelSerializer
from .LoanOfficer import LoanOfficerModel, LoanOfficerModelSerializer
from django.contrib.auth.models import User
from django.forms import forms
from rest_framework import serializers

USER_CATEGORIES_CHOICES = (
    ('ADMIN', 'System Admin'),
    ('BENEFICIARY', 'Beneficiary User Category'),
    ('EMPLOYER', 'Employer User Category'),
    ('LOAN_OFFICER', 'Loan Officer User Category'),
)


class UserCategory(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    employer = models.ForeignKey(EmployerModel, null=True, blank=True, on_delete=models.RESTRICT,
                                 related_name='employer')
    beneficiary = models.ForeignKey(BeneficiaryModel, null=True, blank=True, on_delete=models.RESTRICT,
                                    related_name='beneficiary')
    loan_officer = models.ForeignKey(LoanOfficerModel, null=True, blank=True, on_delete=models.RESTRICT,
                                     related_name='loan_officer')
    category = models.CharField(max_length=30, blank=False, default='BENEFICIARY', choices=USER_CATEGORIES_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.beneficiary is not None:
            return self.category + '-' + self.beneficiary.index_no
        elif self.employer is not None:
            return self.category + '-' + self.employer.employer_name
        elif self.loan_officer is not None:
            return self.category + '-' + self.loan_officer.username
        else:
            return self.user.username

    class Meta:
        verbose_name = 'UserCategory',
        verbose_name_plural = 'UserCategories'
        db_table = 'tbl_user_mgt_user_categories'

    def save(self, *args, **kwargs):
        if (self.category == 'BENEFICIARY' and self.beneficiary is None) or (
                self.category == 'EMPLOYER' and self.employer is None) or (
                self.category == 'LOAN_OFFICER' and self.loan_officer is None):
            raise forms.ValidationError(
                {'error': _(f'When A Benef Or Employer Or Loan Officer Category Is Selected They Should Be Provided')})
        else:
            return super().save(*args, **kwargs)


class UserCategorySerializer(serializers.ModelSerializer):
    beneficiary = BeneficiaryModelSerializer()
    employer = EmployerModelSerializer()
    loan_officer = LoanOfficerModelSerializer()

    class Meta:
        model = UserCategory
        fields = [
            'category',
            'updated_at',
            'employer',
            'beneficiary',
            'loan_officer'
        ]
