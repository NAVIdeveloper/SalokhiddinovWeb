from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Developer)
admin.site.register(AboutWork)
admin.site.register(Bio)
admin.site.register(BioCell)
admin.site.register(Platform)

admin.site.register(Work)
admin.site.register(Project)
admin.site.register(Wallpaper)
admin.site.register(Use)
