from django.contrib import admin
from .models import User , Profile
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id' , 'phone_number']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password','role','account_status']
    list_filter = ['account_status','role']
    #Nữa viết lên base_cho kế thừa
    # readonly_fields = ['img']
    # def img(self, course):
    #     if course:
    #         return mark_safe(
    #             '<img src="/static/{url}" width="120" />' \
    #                 .format(url=course.image.name)
    #         )
admin.site.register(Profile,ProfileAdmin)
admin.site.register(User,UserAdmin)

# class Media:
# css = {
# 'all': ('/static/css/style.css', )
# }
# js = ('/static/js/script.js', )

#Chỉnh sửa nâng cao
# content = RichTextField()