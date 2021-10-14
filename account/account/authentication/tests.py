from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


def user_check_mock(token):
    return False


def token_check_mock(token):
    return {'iss': 'https://dev-kbl8py41.us.auth0.com/', 'sub': 'google-oauth2|114749736464918014590',
            'aud': ['https://dev-kbl8py41.us.auth0.com/api/v2/', 'https://dev-kbl8py41.us.auth0.com/userinfo'],
            'iat': 1634216698, 'exp': 1634303098, 'azp': 'TuE8ekxIxXmr2DTWHYe0X6EUfRjszraQ',
            'scope': 'openid profile email'}


class ViewTests(TestCase):

    def test_get_request_returns_status_401_unauthorized_wrong_token(self):
        client = APIClient()
        user = User()
        user.username = 'testUser'
        user.save()
        client.force_authenticate(user=user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzOTMyNTA2LCJleHAiOjE2MzQwMTg5MDYsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.moiOnhmPaDDUucMO8FsTJfbz8MoPWqqK4uHyUjWwc-3PAi-QA5AyMpA1-mPAYDHuD_l-GvH_6UipgksJ7MHWRUOOFPaxSq8jGsID1D1gg84ItOClg4g7slUjzoR-gJk2rgU0vZj0HcdmfkCA-E0YMyaoEmOcBXo91bRi5VdMaFRHUPCG-jOaIqsUEDntMNucKjPHkYvdh_DvOywrZgsEc8d-a7iYV2B1aIjFOGdLsefmZKH_CnQh5ekF-_U_IQeOXMOn5VNeCxCprqIDgOsuDTz9EII2E0SKZSJw21rfzcbbAEdcFulUAUfpz7w4yAm3-ps3iMY-9xXBkmdCx5GpDQ'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 401)

    def test_get_request_returns_status_401_unauthorized_wrong_admin_user(self):
        client = APIClient()
        token='token'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 401)

    @patch('authentication.views.get_put_delete_view.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.views.get_put_delete_view.jwt_decode_token', side_effect=token_check_mock)
    def test_get_request_returns_status_200(self, mock_user_check, mock_token_check):
        client = APIClient()
        user = User()
        user.username = 'testUser'
        user.save()
        client.force_authenticate(user=user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 200)

    @patch('authentication.views.get_put_delete_view.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.views.get_put_delete_view.jwt_decode_token', side_effect=token_check_mock)
    def test_put_request_returns_status_200(self, mock_user_check, mock_token_check):
        client = APIClient()
        user = User()
        user.username = 'testUser'
        user.save()
        client.force_authenticate(user=user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = client.put('http://localhost:8000/api/account/user', {
                'base_currency': 'USD',
                'first_name': 'Pesho',
                'last_name': 'Peshev',
            })

        self.assertEqual(response.status_code, 200)