from zope.app.component.hooks import getSite
from Acquisition import aq_parent
from Products.PloneFormGen.interfaces import IPloneFormGenForm
from .interfaces import IPfgSoupAdapter
from .storage import PfgCatalogFactory


def create_catalogfactory(obj, event):
    sm = getSite().getSiteManager()
    sm.registerUtility(factory=PfgCatalogFactory, name=obj._soup_name)


def rebuild_catalog(obj, event):
    parent = aq_parent(obj)
    while True:
        if not parent or IPloneFormGenForm.providedBy(parent):
            break
        parent = aq_parent(parent)
    if parent is None:
        return
    sub = None
    for name in parent.contentIds():
        sub = parent[name]
        if IPfgSoupAdapter.providedBy(sub):
            break
    if sub is None:
        return
    soup = sub.get_soup()
    soup.rebuild()
