from django.contrib import admin


class BaseModelWithTimestampsAdmin(admin.ModelAdmin):
    exclude = ['created_by', 'updated_by']
    
    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        
        if not obj.id:
            obj.created_by = request.user
        
        obj.save()