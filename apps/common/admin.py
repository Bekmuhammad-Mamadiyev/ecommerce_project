from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Media)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Settings)
admin.site.register(OurInstagramStory)

class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_position', 'rank']
    search_fields = ['customer_name', 'customer_position']
    list_filter = ['rank']

    def has_add_permission(self, request):
        return False

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)