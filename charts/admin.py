from django.contrib import admin
from .models import HP,projects,sub_projects
# Register your models here.
admin.site.register(HP)
admin.site.register(projects)
admin.site.register(sub_projects)