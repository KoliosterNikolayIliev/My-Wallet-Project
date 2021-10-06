from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Edit profile data
# Needs research for using REST Generic views
@csrf_exempt
def edit_user_profile():
    return JsonResponse('Ready_to_edit', status=200, safe=False)
