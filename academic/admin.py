from django.contrib import admin

from .models import Talk, Paper, Teaching

admin.site.register(Talk)
admin.site.register(Paper)
admin.site.register(Teaching)