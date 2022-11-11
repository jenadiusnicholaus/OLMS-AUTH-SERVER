from django.db import models
from django.utils.translation import gettext as _

from .Employer import EmployerModel
from .Beneficiary import BeneficiaryModel
from django.contrib.auth.models import User
from django.forms import forms

USER_CATEGORIES_CHOICES = (
    ('ADMIN', 'System Admin'),
    ('BENEFICIARY', 'Beneficiary User Category'),
    ('EMPLOYER', 'Employer User Category')
)


class UserCategory(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    employer = models.ForeignKey(EmployerModel, null=True, blank=True, on_delete=models.RESTRICT)
    beneficiary = models.ForeignKey(BeneficiaryModel, null=True, blank=True, on_delete=models.RESTRICT)
    category = models.CharField(max_length=30, blank=False, default='BENEFICIARY', choices=USER_CATEGORIES_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.beneficiary is not None:
            return self.category + '-' + self.beneficiary.index_no
        elif self.employer is not None:
            return self.category + '-' + self.employer.employer_name
        else:
            return self.user.username

    class Meta:
        verbose_name = 'UserCategory',
        verbose_name_plural = 'UserCategories'
        db_table = 'tbl_user_mgt_user_categories'

    def save(self, *args, **kwargs):
        if (self.category == 'BENEFICIARY' and self.beneficiary is None) or (
                self.category == 'EMPLOYER' and self.employer is None):
            raise forms.ValidationError(
                {'error': _(f'When A Benef Or Employer Category Is Selected They Should Be Provided')})
        else:
            return super().save(*args, **kwargs)
