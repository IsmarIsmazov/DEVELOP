from api import mixins
from rest_framework.generics import GenericAPIView


class CustomGenericAPIView(GenericAPIView):
    create_serializer_class = None
    update_serializer_class = None
    validate_serializer_class = None
    retrieve_serializer_class = None
    serializer_class = None
    service_class = None
    prefetch_ = None
    select_ = None


class CustomListAPIView(mixins.ListModelMixin,
                        CustomGenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomCreateAPIView(mixins.CreateModelMixin,
                          CustomGenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomListCreateAPIView(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              CustomGenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomRetrieveAPIView(mixins.RetrieveModelMixin,
                            CustomGenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CustomDestroyAPIView(mixins.DestroyModelMixin,
                           CustomGenericAPIView):
    """
    Concrete view for deleting a model instance.
    """

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomUpdateAPIView(mixins.UpdateModelMixin,
                          CustomGenericAPIView):
    """
    Concrete view for updating a model instance.
    """

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CustomRetrieveUpdateAPIView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  CustomGenericAPIView):
    """
    Concrete view for retrieving, updating a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CustomRetrieveDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin,
                                   CustomGenericAPIView):
    """
    Concrete view for retrieving or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         CustomGenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
