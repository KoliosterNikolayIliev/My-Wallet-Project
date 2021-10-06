from flask import (Blueprint, jsonify)
import os, requests
from ..utils.extensions import scheduler

# store latest prices for crypto
crypto_prices_store = {}

MOCK_ENVIRONMENT = os.environ.get('MOCK_ENVIRONMENT')

# create blueprint
bp = Blueprint('crypto', __name__, url_prefix='/crypto')

def fetch_crypto_price_data():
    global crypto_prices_store
    if not MOCK_ENVIRONMENT:
      req = requests.get('http://api.coinlayer.com/live', params={'access_key': os.environ['CL_API_KEY']})
      res = req.json()

      # if there is an error, print the error message, else update the crypto_prices_store
      try:
          res_body = res['rates']
          for res_key, res_value in res_body.items():
              crypto_prices_store[res_key] = res_value
      except:
          print(f"Error: {res['error']['info']}")
    else:
      crypto_prices_store = {
        "ABC": 59.99,
        "ACP": 0.014931,
        "ACT": 0.007788,
        "ACT*": 0.017178,
        "ADA": 2.219219,
        "ADCN": 0.00013,
        "ADL": 0.01515,
        "ADX": 0.552518,
        "ADZ": 0.0023,
        "AE": 0.1069,
        "AGI": 0,
        "AIB": 0.005626,
        "AIDOC": 0.000957,
        "AION": 0.1573,
        "AIR": 0.001506,
        "ALT": 0.565615,
        "AMB": 0.031387,
        "AMM": 0.0185,
        "ANT": 4.8637,
        "APC": 0.0017,
        "APPC": 0.063585,
        "ARC": 0.0169,
        "ARCT": 0.00061,
        "ARDR": 0.318439,
        "ARK": 1.736165,
        "ARN": 0.040558,
        "ASAFE2": 0.4,
        "AST": 0.260445,
        "ATB": 0.017,
        "ATM": 14.3351,
        "AURS": 0.352867,
        "AVT": 0,
        "BAR": 16.26,
        "BASH": 0.0056,
        "BAT": 0.711219,
        "BAY": 0.0644,
        "BBP": 0.0005,
        "BCD": 1.889855,
        "BCH": 551.141546,
        "BCN": 0.000318,
        "BCPT": 0.003111,
        "BEE": 1.0e-6,
        "BIO": 0.0008,
        "BLC": 0.072132,
        "BLOCK": 1.016,
        "BLU": 0.00054,
        "BLZ": 0.2432,
        "BMC": 0.056704,
        "BNB": 425.622972,
        "BNT": 3.830626,
        "BOST": 0.048,
        "BQ": 7.775e-5,
        "BQX": 2.720931,
        "BRD": 0.167312,
        "BRIT": 0.03,
        "BT1": 0,
        "BT2": 0,
        "BTC": 49445.780732,
        "BTCA": 0.00036,
        "BTCS": 0.01201,
        "BTCZ": 0.000749,
        "BTG": 58.248707,
        "BTLC": 9,
        "BTM": 0.078282,
        "BTM*": 0.122609,
        "BTQ": 0.01,
        "BTS": 0.04439,
        "BTX": 0.292581,
        "BURST": 0.017348,
        "CALC": 0.0006,
        "CAS": 0.007,
        "CAT": 0.150318,
        "CCRB": 0.08888,
        "CDT": 0.109038,
        "CESC": 0.0037,
        "CHAT": 0.001414,
        "CJ": 0.000898,
        "CL": 0.028,
        "CLD": 0.02,
        "CLOAK": 10,
        "CMT*": 0.03954,
        "CND": 0.015482,
        "CNX": 1.996594,
        "CPC": 0.0005,
        "CRAVE": 0.4,
        "CRC": 0.08475,
        "CRE": 1.316485,
        "CRW": 0.05402,
        "CTO": 0.005,
        "CTR": 0.017,
        "CVC": 0.512215,
        "DAS": 0.937816,
        "DASH": 176.269394,
        "DAT": 0.059509,
        "DATA": 0.11787,
        "DBC": 0.005436,
        "DBET": 0.027656,
        "DCN": 2.15e-5,
        "DCR": 122.785936,
        "DCT": 0.006819,
        "DEEP": 0.001,
        "DENT": 0.005957,
        "DGB": 0.048102,
        "DGD": 652.77688,
        "DIM": 9.4957e-5,
        "DIME": 3.0e-5,
        "DMD": 0.58782,
        "DNT": 0.15848,
        "DOGE": 0.230592,
        "DRGN": 0.152195,
        "DRZ": 3,
        "DSH": 252.13175,
        "DTA": 0.000338,
        "EC": 50,
        "EDG": 0.0094,
        "EDO": 1.0077,
        "EDR": 0,
        "EKO": 0.000988,
        "ELA": 4.5175,
        "ELF": 0.67196,
        "EMC": 0.069674,
        "EMGO": 0.43382,
        "ENG": 0.075613,
        "ENJ": 1.606968,
        "EOS": 4.579627,
        "ERT": 0.2054,
        "ETC": 52.351598,
        "ETH": 3420.52487,
        "ETN": 0.02003,
        "ETP": 0.158069,
        "ETT": 2.9,
        "EVR": 0.104931,
        "EVX": 0.685071,
        "FCT": 1.614358,
        "FLP": 0.0087,
        "FOTA": 0.000509,
        "FRST": 0.78001,
        "FUEL": 0.000634,
        "FUN": 0.019055,
        "FUNC": 0.00061,
        "FUTC": 0.004,
        "GAME": 0.128313,
        "GAS": 8.489576,
        "GBYTE": 26.26852,
        "GMX": 6.467e-5,
        "GNO": 272.72,
        "GNT": 0.511213,
        "GNX": 0.014332,
        "GRC": 0.0067,
        "GRS": 10,
        "GRWI": 10000,
        "GTC": 8.166184,
        "GTO": 0.03677,
        "GUP": 0.001202,
        "GVT": 3.600759,
        "GXS": 0.39381,
        "HAC": 0.001128,
        "HNC": 0,
        "HSR": 1.8723,
        "HST": 0.0027,
        "HVN": 0.03529,
        "ICN": 0.1452,
        "ICOS": 17,
        "ICX": 2.187844,
        "IGNIS": 0.02257,
        "ILC": 0.098703,
        "INK": 0.000877,
        "INS": 0.305417,
        "INSN": 0.0473,
        "INT": 0.019,
        "IOP": 15.455555,
        "IOST": 0.053955,
        "ITC": 0.05793,
        "KCS": 10.2,
        "KICK": 0.000324,
        "KIN": 7.17295e-5,
        "KLC": 0.000703,
        "KMD": 1.030039,
        "KNC": 1.658068,
        "KRB": 6,
        "LA": 0.116251,
        "LEND": 3.146689,
        "LEO": 2.929403,
        "LINDA": 0.000271,
        "LINK": 26.887602,
        "LOC": 6.484134,
        "LOG": 0.060174,
        "LRC": 0.40139,
        "LSK": 3.291234,
        "LTC": 168.073631,
        "LUN": 0.160102,
        "LUX": 2.09e-6,
        "MAID": 0.554314,
        "MANA": 0.795132,
        "MCAP": 0.005398,
        "MCO": 8.95,
        "MDA": 0.73627,
        "MDS": 0.004967,
        "MIOTA": 1.2234,
        "MKR": 2472.660023,
        "MLN": 139.723,
        "MNX": 0.028649,
        "MOD": 1.0148,
        "MOIN": 0.033073,
        "MONA": 1.444725,
        "MTL": 3.35075,
        "MTN*": 0.009575,
        "MTX": 0.022981,
        "NAS": 0.375261,
        "NAV": 0.379068,
        "NBT": 64.651231,
        "NDC": 0.008989,
        "NEBL": 1.262687,
        "NEO": 43.424121,
        "NEU": 0.158324,
        "NEWB": 0.002604,
        "NGC": 0.133091,
        "NKC": 0.002463,
        "NLC2": 0.599935,
        "NMC": 5.867998,
        "NMR": 44.850494,
        "NULS": 0.4566,
        "NVC": 10,
        "NXT": 0.01639,
        "OAX": 0.183318,
        "OBITS": 0.015,
        "OC": 0.000868,
        "OCN": 0.000696,
        "ODN": 0.5,
        "OK": 0.030143,
        "OMG": 17.019058,
        "OMNI": 3.0142,
        "ORE": 0,
        "ORME": 1.235715,
        "OST": 0.003672,
        "OTN": 0,
        "OTX": 0.023,
        "OXY": 2.353,
        "PART": 3.951477,
        "PAY": 0.047933,
        "PBT": 658.689553,
        "PCS": 0.019961,
        "PIVX": 0.749146,
        "PIZZA": 0.001,
        "PLBT": 20,
        "PLR": 0.037343,
        "POE": 0.000148,
        "POLY": 0.9569,
        "POSW": 0.48712,
        "POWR": 0.356783,
        "PPC": 0.756046,
        "PPT": 0.77,
        "PPY": 5.45,
        "PRC": 3.0e-5,
        "PRES": 0.219998,
        "PRG": 0.4,
        "PRL": 0.061361,
        "PRO": 0.947386,
        "PURA": 0.25,
        "PUT": 0,
        "QASH": 0.07091,
        "QAU": 0,
        "QSP": 0.053868,
        "QTUM": 13.681817,
        "QUN": 0.008318,
        "R": 1,
        "RBIES": 1,
        "RCN": 0.024275,
        "RDD": 0.002712,
        "RDN": 0,
        "RDN*": 0.324446,
        "REBL": 0.003624,
        "REE": 1.0e-5,
        "REP": 24.3835,
        "REQ": 0.20525,
        "REV": 0.018477,
        "RGC": 0.001,
        "RHOC": 0.178417,
        "RIYA": 0.090025,
        "RKC": 5,
        "RLC": 3.827704,
        "RPX": 0.110688,
        "RUFF": 0.003978,
        "SALT": 0.768708,
        "SAN": 0.224793,
        "SBC": 7,
        "SC": 0.016089,
        "SENT": 0.0073,
        "SHIFT": 0,
        "SIB": 5.177,
        "SMART": 0.005218,
        "SMLY": 6.0e-5,
        "SMT*": 0.011226,
        "SNC": 0.031356,
        "SNGLS": 0.000414,
        "SNM": 0.163087,
        "SNT": 0.082403,
        "SPK": 0.0084,
        "SRN": 0.008982,
        "STEEM": 0.54151,
        "STK": 0.001483,
        "STORJ": 1.212392,
        "STRAT": 0.79056,
        "STU": 0.00019,
        "STX": 0.6985,
        "SUB": 0.002622,
        "SUR": 0.306474,
        "SWFTC": 0.00153,
        "SYS": 0.307356,
        "TAAS": 10,
        "TESLA": 0.019139,
        "THC": 0.010871,
        "THETA": 5.971786,
        "THS": 0.00171,
        "TIO": 0.085,
        "TKN": 0,
        "TKY": 0.000825,
        "TNB": 0.002524,
        "TNT": 0.020536,
        "TOA": 0.002397,
        "TRC": 6.2,
        "TRIG": 0.978399,
        "TRST": 0.04799,
        "TRUMP": 0.055,
        "TRX": 0.093413,
        "UBQ": 0.300305,
        "UNO": 90.0011,
        "UNRC": 6.0e-5,
        "UQC": 13.005,
        "USDT": 1.003018,
        "UTK": 0.361922,
        "UTT": 0.274399,
        "VEE": 0.01,
        "VEN": 6.882656,
        "VERI": 23.736235,
        "VIA": 0.191727,
        "VIB": 0.043833,
        "VIBE": 0.012355,
        "VOISE": 0.00018,
        "VOX": 1360.21674,
        "VRS": 0.1375,
        "VTC": 0.491176,
        "VUC": 9.9e-5,
        "WABI": 0.196544,
        "WAVES": 26.412277,
        "WAX": 0.299,
        "WC": 0.045,
        "WGR": 0.041014,
        "WINGS": 0.035084,
        "WLK": 0.0058,
        "WOP": 0.046453,
        "WPR": 0.00893,
        "WRC": 0.00055,
        "WTC": 0.9112,
        "XAUR": 0.10301,
        "XBP": 0.0027,
        "XBY": 0.2889,
        "XCP": 19.765628,
        "XCXT": 0.095658,
        "XDN": 0.000949,
        "XEM": 0.159228,
        "XGB": 0.0015,
        "XHI": 0.001325,
        "XID": 0.010924,
        "XLM": 0.306727,
        "XMR": 262.090273,
        "XNC": 0.00018,
        "XRB": 43.81641,
        "XRP": 1.05152,
        "XTO": 0.324858,
        "XTZ": 8.455061,
        "XUC": 0.100158,
        "XVG": 0.022422,
        "XZC": 4.96985,
        "YEE": 0.001094,
        "YOC": 0.00012,
        "YOYOW": 0.019768,
        "ZBC": 0,
        "ZCL": 0.152201,
        "ZEC": 117.092809,
        "ZEN": 74.997263,
        "ZIL": 0.098856,
        "ZNY": 0.02,
        "ZRX": 0.981846,
        "ZSC": 0.000301,
        "611": 0.389165
    }
    

# fetch price data for crypto the first time the server goes live
scheduler.add_job(func=fetch_crypto_price_data, id='crypto_price_update', max_instances=1)

# fetch price data for crypto every 24 hours
scheduler.add_job(func=fetch_crypto_price_data, trigger='interval', seconds=86400, id='periodic_crypto_price_update')

# microservice endpoint to return the latest prices for crypto
@bp.route('/prices', methods=(['GET']))
def prices():
    """
    ---
    get:
      description: Request latest price data for available cryptocurrencies
      responses:
        '200':
          description: A successful call was made and the results were returned
          content:
            application/json:
              schema: OutputSchema
              example:
                ADA: 2.314212
                BTC: 47039.2419
    
    """
    if crypto_prices_store:
        return jsonify(crypto_prices_store)
    fetch_crypto_price_data()
    return jsonify(crypto_prices_store)
