from pyramid.renderers import get_renderer
from pyramid.view import view_config
from ..resources import Item

@view_config(
    renderer='templates/splash.pt',
    )
def splash_view(request):
    manage_prefix = request.registry.settings.get('substanced.manage_prefix',
                                                  '/manage')
    return {'manage_prefix': manage_prefix}

@view_config(
    context=Item,
    renderer='templates/item.pt',
    )
def document_view(context, request):
    return {'name': context.name,
            'title': context.title,
            'master': get_renderer('templates/master.pt').implementation(),
           }
