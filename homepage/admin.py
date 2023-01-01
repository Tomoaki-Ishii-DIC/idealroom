from django.contrib import admin
from .models import Coordinator#追加
from .models import Coordinator2#追加

# Register your models here.
#管理サイトで操作
admin.site.register(Coordinator)
admin.site.register(Coordinator2)