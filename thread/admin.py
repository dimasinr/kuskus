from django.contrib import admin
from .models import Thread, ThreadComment

admin.site.register(Thread)
admin.site.register(ThreadComment)