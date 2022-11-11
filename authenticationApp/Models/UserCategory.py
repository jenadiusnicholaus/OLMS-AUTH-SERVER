from django.db import models
from django.db.models import Q

from .Employer import EmployerModel
from .Beneficiary import BeneficiaryModel
from django.contrib.auth.models import User

USER_CATEGORIES = (
    ('ADMIN', 'System Admin'),
    ('BENEFICIARY', 'Beneficiary User Category'),
    ('EMPLOYER', 'Employer User Category')
)


class UserCategory(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    employer = models.ForeignKey(EmployerModel, null=True, on_delete=models.RESTRICT)
    beneficiary = models.ForeignKey(BeneficiaryModel, null=True, on_delete=models.RESTRICT)
    category = models.CharField(max_length=30, blank=False, default='BENEFICIARY', )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category + '-' + self.employer.employer_name + self.beneficiary.index_no

    class Meta:
        db_table = 'tbl_user_mgt_user_categories'
        constraints = [
            models.CheckConstraint(
                check=Q(category='BENEFICIARY') & Q(beneficiary__isnull=True),
                name='benef_category_must_have_a_benef'
            ),
            models.CheckConstraint(
                check=Q(category='EMPLOYER') & Q(beneficiary__isnull=True),
                name='employer_category_must_have_an_employer'
            )
        ]
