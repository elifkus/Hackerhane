import json
from django.http import HttpResponse
from django.views.generic.list import BaseListView
from jqgrid import JqGrid
from accounting.models import Transaction
from django.core.urlresolvers import reverse_lazy

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_to_json(self, context):
        return json.dumps(context)


class JSONListView(JSONResponseMixin, BaseListView):
    
    def render_to_response(self, context, **response_kwargs):  
        object_list= [item.as_dict() for item in list(context['object_list'] )]         
        return self.render_to_json_response(object_list, **response_kwargs)

    
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