from django.http import HttpResponse
from jqgrid import JqGrid
from accounting.models import Transaction
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import FieldError

class CustomJqGrid(JqGrid):
    def field_to_colmodel(self, field, field_name):
        colmodel = super(CustomJqGrid, self).field_to_colmodel(field, field_name)
        
        colmodel['label'] = field.verbose_name.title()
        
        return colmodel
    
    def sort_items(self, request, items):
        sidx = request.GET.get('sidx')
        if sidx is not None:
            #for fields in the related object, we need to have the full name of the field
            if sidx not in self.fields:
                sidx = next((item for item in self.fields if item.endswith('__'+sidx)), sidx)
            
            sord = request.GET.get('sord')
                
            order_by = '%s%s' % (sord == 'desc' and '-' or '', sidx)
            
            try:
                items = items.order_by(order_by)
            except FieldError:
                items = items.order_by('type__'+order_by)
                pass
        return items
    
class TransactionGrid(CustomJqGrid):
    model = Transaction # could also be a queryset
    fields = ['payment_media', 'type__name', 'note', 'amount', 'realized_date'] # optional 
    url = reverse_lazy('grid_handler')
    extra_config = {'sortname': 'realized_date', 'sortorder': 'desc'}
    caption = 'İşlemler' # optional
    colmodel_overrides = {'type__name': {'label':'Type'}, 
                          'realized_date': {'label':'Date', 'formatter':'date', 
                                            'formatoptions':{'newformat':'j M Y',}}}
    
def grid_handler(request):
    # handles pagination, sorting and searching
    grid = TransactionGrid()
    return HttpResponse(grid.get_json(request), mimetype="application/json")

def grid_config(request):
    # build a config suitable to pass to jqgrid constructor   
    grid = TransactionGrid()
    return HttpResponse(grid.get_config(), mimetype="application/json")

