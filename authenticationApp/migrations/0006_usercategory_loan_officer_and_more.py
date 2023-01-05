# Generated by Django 4.1.1 on 2022-11-14 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticationApp', '0005_loanofficermodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercategory',
            name='loan_officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='loan_officer', to='authenticationApp.loanofficermodel'),
        ),
        migrations.AlterField(
            model_name='usercategory',
            name='category',
            field=models.CharField(choices=[('ADMIN', 'System Admin'), ('BENEFICIARY', 'Beneficiary User Category'), ('EMPLOYER', 'Employer User Category'), ('LOAN_OFFICER', 'Loan Officer User Category')], default='BENEFICIARY', max_length=30),
        ),
    ]