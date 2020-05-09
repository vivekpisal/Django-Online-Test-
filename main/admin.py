from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Info)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Members)
admin.site.register(Poll)
admin.site.register(Notice)