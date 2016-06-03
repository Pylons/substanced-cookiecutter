import colander

from persistent import Persistent

from substanced.content import content
from substanced.folder import Folder
from substanced.property import PropertySheet
from substanced.schema import (
    Schema,
    NameSchemaNode
    )
from substanced.util import renamer


def content_columns(folder, subobject, request, default_columnspec):

    return default_columnspec + [
        {'name': 'Title',
         'value': getattr(subobject, 'title', None),
         },
    ]

def context_is_a_content_folder(context, request):
    return request.registry.content.istype(context, 'ContentFolder')

class ContentFolderSchema(Schema):
    name = NameSchemaNode(
        editing=context_is_a_content_folder,
        )
    title = colander.SchemaNode(
        colander.String(),
        )

class ContentFolderPropertySheet(PropertySheet):
    schema = ContentFolderSchema()

@content(
    'ContentFolder',
    icon='glyphicon glyphicon-list-alt',
    add_view='add_content_folder',
    columns=content_columns,
)
class ContentFolder(Folder):

    __sdi_addable__ = ('Item',)
    name = renamer()

    def __init__(self, name='', title=''):
        super(ContentFolder, self).__init__()
        self.title = title

def context_is_an_item(context, request):
    return request.registry.content.istype(context, 'Item')

class ItemSchema(Schema):
    name = NameSchemaNode(
        editing=context_is_an_item,
        )
    title = colander.SchemaNode(
        colander.String(),
        )

class ItemPropertySheet(PropertySheet):
    schema = ItemSchema()

def maybe_add_item(context, request):
    if request.registry.content.istype(context, 'ContentFolder'):
        return 'add_item'

@content(
    'Item',
    icon='glyphicon glyphicon-book',
    add_view=maybe_add_item,
    )
class Item(Persistent):

    name = renamer()

    def __init__(self, name='', title=''):
        self.title = title

def includeme(config): # pragma: no cover
    config.add_propertysheet('Basic', ContentFolderPropertySheet, ContentFolder)
    config.add_propertysheet('Basic', ItemPropertySheet, Item)
