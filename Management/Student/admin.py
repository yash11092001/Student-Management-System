from django.contrib import admin
from Student.models import Details
class detailsAdmin(admin.ModelAdmin):
    list_display = ('name','city','course','fee_amount','ad_date')

# Register your models here.
admin.site.register(Details,detailsAdmin)
