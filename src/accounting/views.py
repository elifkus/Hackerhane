from django.http import HttpResponse
from jqgrid import JqGrid
from accounting.models import Transaction
from django.core.urlresolvers import reverse_lazy

    
class TransactionGrid(JqGrid):
    model = Transaction # could also be a queryset
    fields = ['id', 'payment_media', 'type', 'note', 'amount', 'realized_date'] # optional 
    url = reverse_lazy('grid_handler')
    caption = 'İşlemler' # optional
    colmodel_overrides = {
        'id': { 'editable': False, 'width':10 },
    }


def grid_handler(request):
    # handles pagination, sorting and searching
    grid = TransactionGrid()
    return HttpResponse(grid.get_json(request), mimetype="application/json")

def grid_config(request):
    # build a config suitable to pass to jqgrid constructor   
    grid = TransactionGrid()
    return HttpResponse(grid.get_config(), mimetype="application/json")