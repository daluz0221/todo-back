from django.contrib import admin

from .models import User  # Import your User model here

# Register your models here.


admin.site.site_header = "TodoBack Admin"
admin.site.site_title = "TodoBack Admin Portal"
admin.site.index_title = "Welcome to the TodoBack Admin Portal"
admin.register(User)(admin.ModelAdmin)  # Register the User model with the admin site