__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '29/11/18'

from django.http.response import Http404, HttpResponseBadRequest
from rest_framework.response import Response
from api.api_views.v2.facilities.base_api import (
    BaseAPI
)
from localities.models import Locality


class GetDetailFacility(BaseAPI):
    """
    get:
    Returns a facility detail.

    put:
    Update a facility.
    There are mandatory field for this:
    1. uuid : this is path parameters
    """

    def get(self, request, uuid):
        try:
            facility = Locality.objects.get(uuid=uuid)
            return Response(self.serialize(facility))
        except Locality.DoesNotExist:
            raise Http404()

    def put(self, request, uuid):
        try:
            data = request.data
            facility = Locality.objects.get(uuid=uuid)
            try:
                facility.update_data(data, request.user)
                return Response('OK')
            except KeyError as e:
                return HttpResponseBadRequest('%s is required' % e)
            except ValueError as e:
                return HttpResponseBadRequest('%s' % e)
        except Locality.DoesNotExist:
            raise Http404()
