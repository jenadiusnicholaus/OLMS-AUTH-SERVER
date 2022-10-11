from rest_framework.views import APIView
from rest_framework.response import Response

from ..CustomMixins.AuthAppResponseMixins import AuthAppHttpResponseMixins
from ..Serializers import EmployerSerializers
from ...Models import EmployerModels


class EmployerLoginView(APIView, AuthAppHttpResponseMixins):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        req_param = self.request.GET.get('tin')
        if req_param is None or req_param == '':
            return self.render_to_auth_app_http_response(None, False, 'Required Query Parameter Tin is Missing', 400)
        qs = EmployerModels.EmployerModel.objects.filter(tin__exact=req_param)
        if qs.exists():
            sz = EmployerSerializers.EmployerLoginSerializer(qs, many=True)
            return Response(sz.data, status=200)
        else:
            return self.render_to_auth_app_http_response \
                (None, False, f'Sorry We Don\'t Recognize This Tin {req_param}', 400)
