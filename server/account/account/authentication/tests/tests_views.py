from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from authentication.models import UserProfile


def user_check_mock(token):
    return False


def token_check_mock(token):
    return {'iss': 'https://dev-kbl8py41.us.auth0.com/', 'sub': 'google-oauth2|114749736464918014590',
            'aud': ['https://dev-kbl8py41.us.auth0.com/api/v2/', 'https://dev-kbl8py41.us.auth0.com/userinfo'],
            'iat': 1634216698, 'exp': 1634303098, 'azp': 'TuE8ekxIxXmr2DTWHYe0X6EUfRjszraQ',
            'scope': 'openid profile email'}


class ViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User()

    def test_get_request_returns_status_401_unauthorized_wrong_token(self):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjMzOTMyNTA2LCJleHAiOjE2MzQwMTg5MDYsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.moiOnhmPaDDUucMO8FsTJfbz8MoPWqqK4uHyUjWwc-3PAi-QA5AyMpA1-mPAYDHuD_l-GvH_6UipgksJ7MHWRUOOFPaxSq8jGsID1D1gg84ItOClg4g7slUjzoR-gJk2rgU0vZj0HcdmfkCA-E0YMyaoEmOcBXo91bRi5VdMaFRHUPCG-jOaIqsUEDntMNucKjPHkYvdh_DvOywrZgsEc8d-a7iYV2B1aIjFOGdLsefmZKH_CnQh5ekF-_U_IQeOXMOn5VNeCxCprqIDgOsuDTz9EII2E0SKZSJw21rfzcbbAEdcFulUAUfpz7w4yAm3-ps3iMY-9xXBkmdCx5GpDQ'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 401)

    def test_get_request_returns_status_401_unauthorized_wrong_admin_user(self):
        token = 'token'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 401)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_get_request_returns_status_200_user_not_existing(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 200)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_get_request_returns_status_200_user_existing(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        user_account = UserProfile()
        user_account.user_identifier = 'google-oauth2|114749736464918014590'
        user_account.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/user', )

        self.assertEqual(response.status_code, 200)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_get_request_internal_returns_status_200_not_existing(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/internal/user', )

        self.assertEqual(response.status_code, 200)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_get_request_internal_returns_status_200_user_existing(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        user_account = UserProfile()
        user_account.user_identifier = 'google-oauth2|114749736464918014590'
        user_account.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('http://localhost:8000/api/account/internal/user', )

        self.assertEqual(response.status_code, 200)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_put_request_returns_status_404_not_existing_user(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.put('http://localhost:8000/api/account/user', {
            'base_currency': 'USD',
            'first_name': 'Pesho',
            'last_name': 'Peshev',
        })

        self.assertEqual(response.status_code, 404)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_put_request_returns_status_200_successful_edit(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        user_account = UserProfile()
        user_account.user_identifier = 'google-oauth2|114749736464918014590'
        user_account.save()
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.put('http://localhost:8000/api/account/user', {
            'base_currency': 'USD',
            'first_name': 'Pesho',
            'last_name': 'Peshev',
        })

        self.assertEqual(response.status_code, 200)

    @patch('authentication.common_shared.utils.user_does_not_exist', side_effect=user_check_mock)
    @patch('authentication.common_shared.utils.jwt_decode_token', side_effect=token_check_mock)
    def test_delete_request_returns_status_204(self, mock_user_check, mock_token_check):
        self.user.username = 'testUser'
        self.user.save()
        self.client.force_authenticate(user=self.user)
        user_account = UserProfile()
        user_account.user_identifier = 'google-oauth2|114749736464918014590'
        user_account.save()
        token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVyN0FyLXF2MU1SV2hIWnNIenhFMiJ9.eyJpc3MiOiJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ3NDk3MzY0NjQ5MTgwMTQ1OTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXYta2JsOHB5NDEudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL2Rldi1rYmw4cHk0MS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjM0MjE2Njk4LCJleHAiOjE2MzQzMDMwOTgsImF6cCI6IlR1RThla3hJeFhtcjJEVFdIWWUwWDZFVWZSanN6cmFRIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCJ9.EOmXf6kSrMG1U0snGChOru-gutnlUIxIbatVBiNrVrfLEBxyHV55kzSl0wWtHvZ1qjWpdgMAqZtMOjgTrG0eJr5NLHf0lev6S0cCcwJ4ZhutBQ36AenRHq6Snfwe7WwyGZykfODdteXJbUq3A8b4Ob6L9JxQLc_-kUx3qfe8BzoVs2xSEp5tBt5DduVUMHMI1OwN-Ufeji6roY7f4vAxG3kav0TcCcPRXR_LlMUBXyCXz8SK-5RnF0YIjlK57pIU0UbAOxOxmmaC_0x8QnH3so0saNoZFRmLKOFs2-G8VPnjN3yY3tul6R44pZhHeVD3eOFXVzDmPQcIcgVs5LiDJA'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.delete('http://localhost:8000/api/account/user')

        self.assertEqual(response.status_code, 204)
