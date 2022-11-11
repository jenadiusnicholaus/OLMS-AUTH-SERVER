from django.contrib import admin
from .Models import Employer, Beneficiary, UserCategory, Regions, Sectors


# Register your models here.
@admin.register(Employer.EmployerModel)
class EmployerModel(admin.ModelAdmin):
    list_per_page = 50  # how many elements per page
    list_display = ('employer_name', 'short_code', 'tin', 'created_date')  # what fields to show
    ordering = ('-created_date',)  # ordering of the list
    preserve_filters = ('employer_id', 'short_code')
    # list_filter = ('tin',)  # list filters on the side
    search_fields = ('employer_id', 'short_code')  # traversed fields on the list that will be searched


@admin.register(Beneficiary.BeneficiaryModel)
class BeneficiaryModel(admin.ModelAdmin):
    list_per_page = 50  # how many elements per page
    list_display = ('loanee_id', 'index_no', 'first_name', 'middle_name', 'last_name')  # what fields to show
    ordering = ('-created_date',)
    preserve_filters = ('index_no', 'loanee_id')
    search_fields = ('index_no', 'loanee_id')


@admin.register(UserCategory.UserCategory)
class UserCategory(admin.ModelAdmin):
    list_per_page = 50  # how many elements per page
    list_display = ('category', 'employer', 'user', 'beneficiary')  # what fields to show
    ordering = ('-created_date',)
    preserve_filters = ('id', 'employer', 'beneficiary')
    search_fields = ('id', 'employer', 'beneficiary')


@admin.register(Regions.RegionModel)
class RegionModel(admin.ModelAdmin):
    list_per_page = 50  # how many elements per page
    list_display = ('region_name',)  # what fields to show
    ordering = ('-created_date',)


@admin.register(Sectors.SectorsModel)
class SectorsModel(admin.ModelAdmin):
    list_per_page = 50  # how many elements per page
    list_display = ('sector_name', 'created_date',)  # what fields to show
    ordering = ('-created_date',)
    preserve_filters = ('sector_name',)
    search_fields = ('sector_name',)
