from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


@csrf_exempt
def mock_data_view(request):
    data = {'balances': [{'balance': 47175.48571080616,
                          'source_balances_history': [{'provider': 'Wise',
                                                       'value': 7561.12},
                                                      {'provider': 'Etoro',
                                                       'value': 25.639474201697197},
                                                      {'provider': 'binance',
                                                       'value': 66.32957751966025},
                                                      {'provider': 'coinbase',
                                                       'value': 1259.7141826595068},
                                                      {'provider': 'custom_assets',
                                                       'value': 38228.44893509205}],
                          'timestamp': '2021-09-05T18:16:38.896000'},
                         {'balance': 47175.48571080616,
                          'source_balances_history': [{'provider': 'Wise',
                                                       'value': 7561.12},
                                                      {'provider': 'Etoro',
                                                       'value': 25.639474201697197},
                                                      {'provider': 'binance',
                                                       'value': 66.32957751966025},
                                                      {'provider': 'coinbase',
                                                       'value': 1259.7141826595068},
                                                      {'provider': 'custom_assets',
                                                       'value': 38228.44893509204}],
                          'timestamp': '2021-12-05T21:49:35.663000'},
                         {'balance': 200001.48571080616,
                          'source_balances_history': [{'provider': 'Wise',
                                                       'value': 7561.12},
                                                      {'provider': 'Etoro',
                                                       'value': 25.639474201697197},
                                                      {'provider': 'binance',
                                                       'value': 66.32957751966025},
                                                      {'provider': 'coinbase',
                                                       'value': 1259.7141826595068},
                                                      {'provider': 'custom_assets',
                                                       'value': 187000.44893509204}],
                          'timestamp': '2021-12-05T21:49:35.663000'}]}

    return JsonResponse(data, safe=False, status=status.HTTP_201_CREATED)
