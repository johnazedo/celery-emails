from django.contrib import admin
from core.models import Email, Message

# Register your models here.
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
