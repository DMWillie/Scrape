import base64
import time
from django.http import HttpResponse
import hashlib


class TokenMiddleware(object):
    """
    use token middleware to encrypt every request
    """
    def __init__(self, get_response):
        """
        define response and max time threshold
        :param get_response:
        """
        self.get_response = get_response
        self.threshold = 180

    def __call__(self, request):
        """
        check token
        :param request:
        :return:
        """
        token = request.GET.get('token')
        path = request.path.rstrip('/')

        # get client sign and time
        string = base64.b64decode(token).decode('utf-8')
        client_sign, client_time = string.split(',')
        server_time = str(int(time.time()))

        # check time
        if abs(int(server_time) - int(client_time)) > self.threshold:
            return HttpResponse(status=401)

        # get server sign
        args = ','.join([path, client_time])
        server_sign = hashlib.sha1(args.encode('utf-8')).hexdigest()

        # check sign
        if server_sign != client_sign:
            return HttpResponse(status=401)
        response = self.get_response(request)
        return response
