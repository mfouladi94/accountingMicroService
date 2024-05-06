import requests
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

AUTH_SERVICE_URL = 'http://auth_service_url'


def extract_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    try:
        return auth_header.split()[1]
    except IndexError:
        return None


def validate_token(token):
    try:
        access_token = AccessToken(token)
        return access_token.payload.get('user_id')
    except Exception as e:
        return None


def verify_authentication(auth_token):
    response = requests.post(AUTH_SERVICE_URL, headers={'Authorization': auth_token})
    return response.status_code == 200


def valid_authorization(request):
    token = extract_token(request)
    if not token:
        return False

    user_id = validate_token(token)
    if not user_id:
        return False

    auth_token = request.META.get('HTTP_AUTHORIZATION')  # Assuming token is passed in the Authorization header
    if verify_authentication(auth_token):

        return True
    else:
        return False


def get_user_id(request):
    try:
        token = extract_token(request)
        if not token:
            return False

        user_id = validate_token(token)
        access_token = AccessToken(token)
        return access_token.payload.get('user_id')
    except Exception as e:
        return None
