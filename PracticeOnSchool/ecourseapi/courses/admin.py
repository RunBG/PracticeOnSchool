from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Courses, Category
# Register your models here.

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Course(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'
class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date','active']
    search_fields = ['id', 'name']
    list_filter = ['created_date', 'name']
    readonly_fields = ['my_imge']
    form = CourseForm

    def my_imge(self, course):
        if course.image:
            return mark_safe(f'<img src="/static/{course.image.name}" width="200" />')

admin.site.register(Category)
admin.site.register(Courses, MyCourseAdmin)