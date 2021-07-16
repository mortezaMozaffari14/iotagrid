from django.contrib import admin

# Register your models here.
from .models import (
                     inputs,
                     outputs,
                     nodes,
                     problem

                     )

 
@admin.register(nodes)
class nodesAdmin(admin.ModelAdmin):
    list_display = ('name','type'
                                    
                   )
    list_filter = ('name',)
    search_fields = ('name',)
    
    #def display_cpes(self, obj):
    #    return ','.join([cpe.URI for cpe in obj.cpes.all()])
    #
    #display_cpes.short_description = 'شناسه ها' 
#
    #def display_cves(self, obj):
    #    return ','.join([cve.name for cve in obj.cves.all()])
    #
    #display_cves.short_description = 'آسیب‌پذیری‌ها' 


@admin.register(inputs)
class inputsAdmin(admin.ModelAdmin):
    list_display = ('input',
                   )
    # search_field = ('cpe__product','cpe__vendor',
    #                 'cpe__version',                     
    #                )
      

@admin.register(outputs)
class outputsAdmin(admin.ModelAdmin):
    list_display = ('output',id
                   )

@admin.register(problem)
class problemAdmin(admin.ModelAdmin):
    list_display = ('problem_tag','id'
                   )