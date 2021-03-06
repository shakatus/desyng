
from django.contrib import admin
from .models import Scale, Point, Raise, Date

#class Scales_Inline(admin.TabularInline):
#	model = Scale

class RaisesInline(admin.TabularInline):
	model = Raise
#admin.site.register(Scale)
admin.site.register(Point)
@admin.register(Scale)

#class PointAdmin(admin.ModelAdmin):
#	inlines = [Scales_Inline]
#	pass
#class RaiseAdmin(admin.ModelAdmin):
#	list_display = ('timestamp','timestamp')
#class RaiseAdmin(form.ModelForm):
#	form = Raise
#
#	fieldsets = (
#		(None,{'fields':('timestamp',),}),
#	)

class ScaleAdmin(admin.ModelAdmin):
	list_display  = ('location', 'point','description')
#	pass
	inlines = [RaisesInline]
class RaiseAdmin(admin.ModelAdmin):
	class Media:
		js = ("js/my_script.js",)
admin.site.register(Raise,RaiseAdmin)
admin.site.register(Date)
# Register your models here.
