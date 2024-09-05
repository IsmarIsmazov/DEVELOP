from typing import Dict

LIST_CREATE = {'get': 'list', 'post': 'create'}
LIST = {'get': 'list'}
LIST_UPDATE = {'get': 'list', 'put': 'update'}

RETRIEVE_PARTIAL = {'get': 'retrieve', 'patch': 'partial_update'}
RETRIEVE_PARTIAL_DELETE = {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
RETRIEVE_UPDATE_DELETE: Dict[str, str] = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
RETRIEVE_UPDATE_PARTIAL_DELETE: Dict[str, str] = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
                                                  'delete': 'destroy'}
RETRIEVE_DELETE = {'get': 'retrieve', 'delete': 'destroy'}
RETRIEVE_UPDATE = {'get': 'retrieve', 'put': 'update'}

RETRIEVE = {'get': 'retrieve'}
DELETE = {'delete': 'destroy'}
UPDATE = {'put': 'update'}
PARTIAL = {'patch': 'partial_update'}

PAGE_SIZE = 10


def get_object(obj, id, prefetch_=None, select_=None):
    return obj.service_class.get({'id': id}, prefetch_, select_)


def get_object_transfer(obj, id, is_in_country=False, prefetch_=None, select_=None):
    return obj.service_class.get({'id': id, 'shipment__isnull': is_in_country}, prefetch_, select_)
