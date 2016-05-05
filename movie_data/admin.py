from django.contrib import admin

from .models import Movies, Users, Reviews


admin.site.register(Movies)
admin.site.register(Users)
admin.site.register(Reviews)