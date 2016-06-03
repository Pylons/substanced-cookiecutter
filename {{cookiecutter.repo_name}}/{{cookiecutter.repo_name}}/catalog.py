"""
This module sets up a ``Substance D`` catalog for searching.
"""
from substanced.catalog import (
    catalog_factory,
    Text,
    indexview,
    indexview_defaults,
    )


@catalog_factory('{{ cookiecutter.repo_name }}')
class CatalogFactory(object):
    """
    The catalog factory will be called at initialization time and will create
    a catalog index for each book field.  We do not add an "id" field,
    because that's handled by the system catalog.
    """
    title = Text()


@indexview_defaults(catalog_name='{{ cookiecutter.repo_name }}')
class CatalogViews(object):
    """
    The catalog views are used by the catalog to get the actual value that we
    want to store for each field. This allows us to examine the value before
    indexing and pass in a modified value if necessary. "indexview_defaults"
    are for setting parameters that will be used in all the class views. Here,
    the views will be set for the catalog named "{{ cookiecutter.repo_name }}",
    which is the one we created above.
    """
    def __init__(self, resource):
        self.resource = resource

    @indexview()
    def title(self, default):
        return getattr(self.resource, 'title', default)
