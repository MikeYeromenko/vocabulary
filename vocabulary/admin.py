from django.contrib import admin

# Register your models here.
from vocabulary import models as md


admin.site.register(md.Word)
