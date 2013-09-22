import json
from django.http import HttpResponse
from django.views.generic.list import BaseListView


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
    
    
