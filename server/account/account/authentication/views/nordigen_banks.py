from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os

COUNTRIES = {
    "Austria": "AT",
    "Croatia": "HR",
    "Denmark": "DK",
    "France": "FR",
    "Hungary": "HU",
    "Italy": "IT",
    "Liechtenstein": "LI",
    "Netherlands": "NL",
    "Portugal": "PT",
    "Slovenia": "SL",
    "United Kingdom": "GB",
    "Belgium": "BE",
    "Cyprus": "CY",
    "Estonia": "EE",
    "Germany": "DE",
    "Ireland": "IE",
    "Latvia": "LV",
    "Luxembourg": "LU",
    "Norway": "NO",
    "Romania": "RO",
    "Spain": "ES",
    "Bulgaria": "BG",
    "Czech Republic": "CZ",
    "Finland": "FI",
    "Greece": "GR",
    "Iceland": "IS",
    "Lithuania": "LT",
    "Malta": "MT",
    "Poland": "PL",
    "Slovakia": "SK",
    "Sweden": "SE",
}


def get_access_token():
    url = os.environ.get('NORDIGEN_GET_TOKEN_URL')
    data = {
        'secret_id': os.environ.get('ASSETS_NORDIGEN_ID'),
        'secret_key': os.environ.get('ASSETS_NORDIGEN_KEY')
    }
    return requests.post(url, data=data).json().get('access')



@api_view(['GET'])
def get_nordigen_banks(request):
    headers_country = request.GET.get('country')
    if not headers_country:
        return Response('Country was not provided', status=status.HTTP_400_BAD_REQUEST)

    country = COUNTRIES.get(headers_country)

    if country:
        token = get_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        params = {'country': country}

        response = requests.get('https://ob.nordigen.com/api/v2/institutions/', headers=headers, params=params)
        return Response(response.json(), status=status.HTTP_200_OK)

    return Response('Invalid country', status=status.HTTP_400_BAD_REQUEST)
