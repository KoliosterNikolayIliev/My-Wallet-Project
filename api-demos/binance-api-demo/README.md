This app is using binance_connector library -> https://github.com/binance/binance-connector-python

Official documentation for Binance API -> https://binance-docs.github.io/apidocs/spot/en/#change-log


# How to use binance demo api

### Step 1 - Create python venv and pip install requirements.txt (or do it in your IDE) :


### Step 2 - in the folder biance-api-demo run python main.py or run the file in your IDE:
Then Follow the instructions in the console.
####NOTE: for accessing options 10 and 11 you need to have API_key and API_Secret registered in
####system environment variables or assigned to variables KEY and SECRET in testnet_setup.py (not recommended)


### Step 3 - Obtain and use API_Key, API_Secret:
    How to generate keys:
    1. Register RSA key -> https://testnet.binance.vision/key/register
    https://testnet.binance.vision/ -> How can I use RSA Keys?

    2. Generate HMAC_SHA256 Key -> https://testnet.binance.vision/key/generate

    3. Save the Generated keys (if you loose the you need to revoke them and create new ones)
        -the needed keys are API key and Secret key generated in step 2.



    How to use env variables:
    - Linux/Mac Terminal:
    export binance_api="your_api_key here in the double quotes"
    export binance_secret="your_api_secret_here here in the double quotes"

    - Windows CMD:

    set binance_api=your_api_key_here
    set binance_secret=your_api_secret_here

    - IDE environment variables - depend on the id (Pycharm{name:value})

    key examples(not real):

    key = "hGLWWbEWRKMLyy5gvo8dbwuufQmgJR88T9QBbWCfwGDO0chT3R1W3znALa18kT6B"
    secret = "qgve977nbhLuuTjobjkcCUy2WiAcCodgW7GZI8PBYWJRwk33ZbrmRVLouEKkmyEK"


####NOTE - the Demo_connector API is still in development. More information regarding the functionality can be obtained from the DocStrings and comments in the code.

    Real test keys for testing purposes:
    
    HMAC_SHA256 Key registered
    
    Save these values right now. They won't be shown ever again!
    
    API Key: hGLWWbEWRKMLIP5gvo8dbwRWfQmgJRZZT9QBbWCfwGDO0chT3R1W3znALa18kT3B
    
    Secret Key: qgve977nb7LuuTUobjkcCUy2WWAcCodgW7GZI8PBYRJRwk33ZbrmRVLouEKkmyEN