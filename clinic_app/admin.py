from django.contrib import admin
from .models import Врач, Пациент, Пожелания_пациентов, Записи_пациентов_к_врачам


admin.site.register(Врач)
admin.site.register(Пациент)
admin.site.register(Пожелания_пациентов)
admin.site.register(Записи_пациентов_к_врачам)
