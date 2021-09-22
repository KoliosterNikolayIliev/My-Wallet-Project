# How to use nordigen api

## Step 1 - [Get Access Token](https://ob.nordigen.com/):
When you generate a access token change the token in demo-code.py
```python
headers = {'Authorization': 'Token YOUR_TOKEN'}
```

## Step 2 - Choose a Bank:
You can get banks by country using the **get_banks_by_country** function:
```python
# this will return json with banks in the UK.
json_response = get_banks_by_country('GB')
```

## Step 3 - Create an end-user agreement - (optional)
Use this step only if you want to specify the length of transaction history you want to retrieve. If you skip this step, by default 90 days of transaction history will be retrieved.

Use the **create_end_user_agreement** function which has these parameters:

**max_historical_days** - the length of the transaction history to be retrieved, default is 90 days

**enduser_id** - a unique end-user ID of someone who's using your services. Usually, it's UUID. We can use the uuid build in module in python.
```python
import uuid
enduser_id = uuid.uuid1()
```

**aspsp_id** - is an id of a bank. You get the bank id information from step 2

**Example**
```python
max_historical_days = 50
enduser_id = uuid.uuid1()
aspsp_id = 'BBVAUK_BBVAGB2L'

json_response = create_end_user_agreement(max_historical_days, enduser_id, aspsp_id)
```

## Step 4 - Create a requisition
First, you need to create a requisition which is a collection of inputs for creating links and retrieving accounts.

Use **create_requisition** function which has these parameters:

**enduser_id** - if you skiped step 3, create a new uuid with the uuid build in module. if you didn't skip step 3 the enduser_id must be the same as step 3

**reference** - additional layer of unique ID defined by you

**redirect** - URL where the end user will be redirected after finishing authentication in ASPSP

**agreements** - is an array of ID(s) from user agreement or an empty array if you didn't create

**user_language** - optional

**Example**

```python
enduser_id = '8234e18b-f360-48cc-8bcf-c8625596d74a' # enduser_id from step 3
reference = 1
redirect = 'https://YourWebSite.com'
agreements = ['2dea1b84-97b0-4cb4-8805-302c227587c8'] # agreements id from step 3

json_response = create_requisition(enduser_id, reference, redirect, agreements)
```

## Step 5 - Build a Link
Create a redirect link for the end user to ASPSP. You need to provide aspsp_id from step 2 (and step 3 if you did not skip it) and requisition_id from step 4.

Use **build_link** function.

**Example**
```python
requisition_id = '8126e9fb-93c9-4228-937c-68f0383c2df7'
aspsp_id = 'BBVAUK_BBVAGB2L'

json_response = build_link(requisition_id, aspsp_id)
```

## Step 6 - List accounts
Once the user is redirected back to the link provided in Step 4.1, the user's bank accounts can be listed. Pass the requisition ID to view the accounts.

Use **list_accounts** function

**Example**
```python
requisition_id = '8126e9fb-93c9-4228-937c-68f0383c2df7'
json_response = list_accounts(requisition_id)
```

## Function you can use after you linked bank account
**get_account_metadata(account_id)**

**get_account_balances(account_id)**

**get_account_details(account_id)**

**get_account_transactions(account_id)**

