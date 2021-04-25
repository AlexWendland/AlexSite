from django.contrib import admin

from .models import *

admin.site.register(Talk)
admin.site.register(Paper)
admin.site.register(Teaching)
admin.site.register(Award)