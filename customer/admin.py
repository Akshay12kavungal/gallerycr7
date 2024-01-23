from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Profile,uploadimage


class ProfileAdmin(admin.ModelAdmin):

	list_display=('Id','Name','Email','Password','Confirm_Password')

	list_per_page=4
	actions=['export_details']



admin.site.register(Profile,ProfileAdmin)

class Upload_image(admin.ModelAdmin):

	list_display=('image','uploaded_at',)

	list_per_page=4
	actions=['export_details']

	def display_image(self, obj):
		return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

	display_image.short_description = 'Image Preview'

admin.site.register(uploadimage,Upload_image)
