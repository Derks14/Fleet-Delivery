from django.contrib import admin

# Register your models here.

from .models import User
from .models import Item
from .models import Comment

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Comment)