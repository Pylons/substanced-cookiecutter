from pyramid.httpexceptions import HTTPFound

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder

from .resources import (
    ItemSchema,
    ContentFolderSchema,
)

@mgmt_view(
    context=IFolder,
    name='add_item',
    tab_title='Add Item',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
    )
class AddItemView(FormView):
    title = 'Add Item'
    schema = ItemSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        name = appstruct.pop('name')
        item = registry.content.create('Item', **appstruct)
        self.context[name] = item
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
            )


@mgmt_view(
    context=IFolder,
    name='add_content_folder',
    tab_title='Add Content Folder',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
    )
class AddContentFolderView(FormView):
    title = 'Add Folder'
    schema = ContentFolderSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        name = appstruct.pop('name')
        folder = registry.content.create('ContentFolder', **appstruct)
        self.context[name] = folder
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
            )
