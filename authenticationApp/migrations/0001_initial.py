# Generated by Django 4.1.1 on 2022-11-11 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeneficiaryModel',
            fields=[
                ('loanee_id', models.BigIntegerField(blank=True, null=True)),
                ('index_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('national_id', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('control_number', models.BigIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('isLoanee', models.BooleanField()),
            ],
            options={
                'verbose_name': ('Beneficiary',),
                'verbose_name_plural': 'Beneficiaries',
                'db_table': 'tbl_beneficiaries',
            },
        ),
        migrations.CreateModel(
            name='EmployerModel',
            fields=[
                ('employer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('employer_name', models.CharField(max_length=100, unique=True)),
                ('tin', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=20)),
                ('postal_address', models.CharField(blank=True, max_length=100, null=True)),
                ('physical_address', models.CharField(max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_position', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_telephone', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_person_email', models.CharField(blank=True, max_length=100, null=True)),
                ('vote_code', models.CharField(blank=True, max_length=100, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True)),
                ('control_number', models.BigIntegerField(blank=True, null=True)),
                ('vote_no', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.IntegerField(choices=[(1, 'PUBLIC EMPLOYERS'), (2, 'CENTRAL GOVERNMENT EMPLOYERS'), (3, 'PRIVATE EMPLOYERS')], default=3)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': ('Employer',),
                'verbose_name_plural': 'Employers',
                'db_table': 'tbl_employers',
            },
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('region_id', models.IntegerField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=100, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': ('Region',),
                'verbose_name_plural': 'Regions',
                'db_table': 'tbl_regions',
            },
        ),
        migrations.CreateModel(
            name='SectorsModel',
            fields=[
                ('sector_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sector_name', models.CharField(max_length=100, unique=True)),
                ('sector_description', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': ('Sector',),
                'verbose_name_plural': 'Sectors',
                'db_table': 'tbl_employer_sectors',
            },
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ADMIN', 'System Admin'), ('BENEFICIARY', 'Beneficiary User Category'), ('EMPLOYER', 'Employer User Category')], default='BENEFICIARY', max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('beneficiary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='authenticationApp.beneficiarymodel')),
                ('employer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='authenticationApp.employermodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('UserCategory',),
                'verbose_name_plural': 'UserCategories',
                'db_table': 'tbl_user_mgt_user_categories',
            },
        ),
        migrations.AddField(
            model_name='employermodel',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authenticationApp.regionmodel'),
        ),
        migrations.AddField(
            model_name='employermodel',
            name='sectors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authenticationApp.sectorsmodel'),
        ),
        migrations.AddConstraint(
            model_name='usercategory',
            constraint=models.CheckConstraint(check=models.Q(('category__exact', 'BENEFICIARY'), ('beneficiary__isnull', True)), name='employer_category_must_have_an_employer'),
        ),
        migrations.AddConstraint(
            model_name='usercategory',
            constraint=models.CheckConstraint(check=models.Q(('category__exact', 'EMPLOYER'), ('employer__isnull', True)), name='benef_category_must_have_a_benef'),
        ),
    ]
