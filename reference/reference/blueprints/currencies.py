import os

from flask import Blueprint, jsonify
import requests

bp = Blueprint('currencies', __name__, url_prefix='/currencies')


@bp.route('/prices/<base>', methods=['GET'])
def prices(base):
    """
        ---
        get:
          description: Get the latest foreign exchange reference rates for base currency given
          responses:
            '200':
              description: A successful call was made and the results were returned
              content:
                application/json:
                  schema: OutputSchema
                  example:
                    "AED": 4.279261,
                    "AFN": 104.246359,
                    "ALL": 121.542845,
        """

    if os.environ.get('REFERENCE_USE_MOCK') != 'True':
        response = requests.get('https://api.exchangerate.host/latest/', params={'base': base}).json()
        if response['base'].lower() != base.lower():
            return jsonify({'Error': 'symbol not found'}), 400

        return jsonify(response['rates']), 200

    else:
        data = {
            "AED": 4.279261,
            "AFN": 104.246359,
            "ALL": 121.542845,
            "AMD": 555.231163,
            "ANG": 2.095138,
            "AOA": 695.480107,
            "ARS": 115.678745,
            "AUD": 1.552494,
            "AWG": 2.097391,
            "AZN": 1.981564,
            "BAM": 1.954436,
            "BBD": 2.330565,
            "BDT": 99.484617,
            "BGN": 1.9524,
            "BHD": 0.439769,
            "BIF": 2312.144473,
            "BMD": 1.1649,
            "BND": 1.562467,
            "BOB": 8.031519,
            "BRL": 6.521427,
            "BSD": 1.165376,
            "BTC": 1.8e-05,
            "BTN": 87.184831,
            "BWP": 12.95332,
            "BYN": 2.837986,
            "BZD": 2.343378,
            "CAD": 1.436014,
            "CDF": 2308.255907,
            "CHF": 1.070763,
            "CLF": 0.034399,
            "CLP": 948.019033,
            "CNH": 7.445362,
            "CNY": 7.447232,
            "COP": 4380.200727,
            "CRC": 730.495053,
            "CUC": 1.165406,
            "CUP": 29.994214,
            "CVE": 110.834446,
            "CZK": 25.519871,
            "DJF": 206.96031,
            "DKK": 7.438142,
            "DOP": 65.41373,
            "DZD": 159.777573,
            "EGP": 18.284088,
            "ERN": 17.473494,
            "ETB": 54.916338,
            "EUR": 1,
            "FJD": 2.407049,
            "FKP": 0.843603,
            "GBP": 0.842995,
            "GEL": 3.646695,
            "GGP": 0.842951,
            "GHS": 7.060582,
            "GIP": 0.843136,
            "GMD": 60.572083,
            "GNF": 11258.313728,
            "GTQ": 8.994959,
            "GYD": 243.34812,
            "HKD": 9.056718,
            "HNL": 28.027079,
            "HRK": 7.505314,
            "HTG": 115.667805,
            "HUF": 362.510962,
            "IDR": 16476.498697,
            "ILS": 3.742171,
            "IMP": 0.842751,
            "INR": 87.082947,
            "IQD": 1697.336158,
            "IRR": 49152.846366,
            "ISK": 149.937033,
            "JEP": 0.843385,
            "JMD": 175.563957,
            "JOD": 0.826197,
            "JPY": 132.891155,
            "KES": 129.099229,
            "KGS": 98.773117,
            "KHR": 4733.711306,
            "KMF": 492.606667,
            "KPW": 1048.345514,
            "KRW": 1370.894585,
            "KWD": 0.351775,
            "KYD": 0.96929,
            "KZT": 495.892648,
            "LAK": 11780.195136,
            "LBP": 1775.083626,
            "LKR": 233.095111,
            "LRD": 185.624977,
            "LSL": 16.859889,
            "LYD": 5.30203,
            "MAD": 10.505633,
            "MDL": 20.326376,
            "MGA": 4602.431019,
            "MKD": 61.571754,
            "MMK": 2185.563673,
            "MNT": 3322.082416,
            "MOP": 9.311586,
            "MRO": 415.844011,
            "MRU": 42.247358,
            "MUR": 49.622145,
            "MVR": 18.009357,
            "MWK": 948.550152,
            "MXN": 23.558546,
            "MYR": 4.84296,
            "MZN": 74.365925,
            "NAD": 16.890992,
            "NGN": 477.813132,
            "NIO": 40.928002,
            "NOK": 9.688755,
            "NPR": 139.222808,
            "NZD": 1.619429,
            "OMR": 0.449474,
            "PAB": 1.164806,
            "PEN": 4.592105,
            "PGK": 4.083706,
            "PHP": 59.220066,
            "PKR": 201.729779,
            "PLN": 4.58082,
            "PYG": 8039.594137,
            "QAR": 4.241645,
            "RON": 4.945102,
            "RSD": 117.476614,
            "RUB": 82.623078,
            "RWF": 1183.321247,
            "SAR": 4.369447,
            "SBD": 9.383018,
            "SCR": 17.036868,
            "SDG": 511.942931,
            "SEK": 10.0109,
            "SGD": 1.565704,
            "SHP": 0.843328,
            "SLL": 12359.528418,
            "SOS": 672.499411,
            "SRD": 24.961897,
            "SSP": 151.730894,
            "STD": 24317.8214,
            "STN": 24.927855,
            "SVC": 10.173828,
            "SYP": 1464.466587,
            "SZL": 16.858187,
            "THB": 38.905872,
            "TJS": 13.122409,
            "TMT": 4.083461,
            "TND": 3.277199,
            "TOP": 2.619624,
            "TRY": 10.772897,
            "TTD": 7.894152,
            "TWD": 32.467863,
            "TZS": 2679.622869,
            "UAH": 30.449426,
            "UGX": 4192.148456,
            "USD": 1.164673,
            "UYU": 51.051685,
            "UZS": 12450.74403,
            "VES": 4.836091,
            "VND": 26464.378333,
            "VUV": 130.037593,
            "WST": 2.99186,
            "XAF": 655.649253,
            "XAG": 0.04884,
            "XAU": 0.001499,
            "XCD": 3.148384,
            "XDR": 0.826234,
            "XOF": 655.649458,
            "XPD": 0.001384,
            "XPF": 119.276495,
            "XPT": 0.001459,
            "YER": 291.498701,
            "ZAR": 16.824092,
            "ZMW": 19.863479,
            "ZWL": 375.075113
        }
        return jsonify(data)
