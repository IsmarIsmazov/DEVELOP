from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from api import get_object, PAGE_SIZE


class ListModelMixin:
    is_paginated = 1
    page_size = PAGE_SIZE
    """
    List a queryset.
    """

    def result(self, request, queryset):
        try:
            self.is_paginated = int(request.query_params.get('is_paginated'))
        except:
            pass
        try:
            self.page_size = int(request.query_params.get('page_size', PAGE_SIZE))
        except:
            pass
        if self.is_paginated and self.pagination_class:
            self.pagination_class.page_size = self.page_size
            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = self.validate_serializer_class(data=request.query_params, context={'user': user})
        serializer.is_valid(raise_exception=True)
        queryset = self.filter_queryset(
            self.service_class.filter(filter_data=serializer.filter_validated_data,
                                      search_data=serializer.search_validated_data,
                                      order_data=serializer.order_validated_data,
                                      prefetch_=self.prefetch_,
                                      select_=self.select_))
        return self.result(request, queryset)


class CreateModelMixin:
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.service_class.create(**serializer.validated_data)
        return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)


class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, **kwargs):
        instance = get_object(self, kwargs['pk'], self.prefetch_, self.select_)
        serializer = self.serializer_class(
            instance) if not self.retrieve_serializer_class else self.retrieve_serializer_class(instance)
        return Response(serializer.data)


class UpdateModelMixin:
    """
    Update a model instance.
    """

    def update(self, request, **kwargs):
        instance = get_object(self, kwargs['pk'], self.prefetch_, self.select_)
        serializer = self.update_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['obj'] = instance
        obj = self.service_class.update(**serializer.validated_data)
        return Response(data=self.serializer_class(obj).data, status=status.HTTP_200_OK)


class DestroyModelMixin:
    """
    Destroy a model instance.
    """

    def destroy(self, request, **kwargs):
        with transaction.atomic():
            instance = get_object(self, kwargs['id'])
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
