from django.contrib import admin

from .models import Consulta , Voto , Invitacion , Opcion



class ChoiceInline(admin.StackedInline):
    model = Opcion
    extra = 3


class ConsultaAdmin(admin.ModelAdmin):
	list_display=['consulta_text','autor','pub_date','end_date']
	fieldsets = [
        (None,               {'fields': ['consulta_text']}),
        ('Date information', {'fields': ['pub_date' ,'end_date']}),
    ]
	inlines = [ChoiceInline]
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(autor=request.user)

class OpcionAdmin(admin.ModelAdmin):
	list_display=['opcion_text','votes','consulta']
	fieldsets = [
        (None,               {'fields': ['consulta_text']}),
        ('Date information', {'fields': ['pub_date' ,'end_date']}),
    ]

admin.site.register(Consulta , ConsultaAdmin)
admin.site.register(Opcion , OpcionAdmin)
admin.site.register(Invitacion)
admin.site.register(Voto)