from django.contrib import admin
from .models import Block
# Register your models here.
@admin.register(Block)
class BlockModelAdmin(admin.ModelAdmin):
  list_display=('id','name','email','mobile','city')
