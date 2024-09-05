from rest_framework.viewsets import ViewSetMixin

from api.generics import CustomGenericAPIView
from api.mixins import *


class CustomGenericViewSet(ViewSetMixin, CustomGenericAPIView):
    """
        The GenericViewSet class does not provide any actions by default,
        but does include the base set of generic view behavior, such as
        the `get_object` and `get_queryset` methods.
    """
    pass


class CustomModelViewSet(ListModelMixin,
                         CreateModelMixin,
                         RetrieveModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         CustomGenericViewSet):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
