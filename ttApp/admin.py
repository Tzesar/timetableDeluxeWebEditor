from django.contrib import admin
from ttApp.models import *

class ttAppAdmin(admin.ModelAdmin):
    exclude = ('GLOBAL_ID',)

# Register your models here.
admin.site.register(TIMETABLE, ttAppAdmin)
admin.site.register(TASK, ttAppAdmin)
admin.site.register(HOLIDAY, ttAppAdmin)
admin.site.register(SUBJECT, ttAppAdmin)
admin.site.register(LESSON, ttAppAdmin)
admin.site.register(TEACHER, ttAppAdmin)
admin.site.register(LOCATION, ttAppAdmin)
admin.site.register(LESSON_TYPE, ttAppAdmin)
admin.site.register(EXAM, ttAppAdmin)
admin.site.register(EXAM_TYPE, ttAppAdmin)
admin.site.register(EXAM_GROUP, ttAppAdmin)

