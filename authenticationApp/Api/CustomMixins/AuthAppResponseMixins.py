from rest_framework.response import Response


class AuthAppHttpResponseMixins(object):
    def render_to_auth_app_http_response(self, data, is_success=True, message=None, status=200):
        data_obj = {
            'is_success': is_success,
            'body': data,
            'detail': message
        }
        return Response(data_obj, status)
