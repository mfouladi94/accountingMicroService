import requests
from rest_framework.response import Response


def valid_authorization(request):
    auth_service_url = 'http://auth-service-url/api/auth/verify-user/'
    auth_token = request.META.get('HTTP_AUTHORIZATION')  # Assuming token is passed in the Authorization header

    response = requests.post(auth_service_url, headers={'Authorization': auth_token})

    if response.status_code == 200:
        # User is authenticated, proceed to create wallet
        # Your wallet creation logic here
        return True
    else:
        return False
