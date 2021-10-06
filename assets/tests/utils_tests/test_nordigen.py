from unittest import TestCase
from utils import nordigen


class NordigenTests(TestCase):
    def setUp(self):
        nordigen.headers = {'Authorization': 'Token 201ad808f1e2dd3136777f56db2568a08fbfc219'}
        self.requisition_id = 'c0ad1b3e-28e1-4628-b8b1-f6009df3c27f'

    def test_validate_requisition__when_requisition_id_is_none__expect_tuple_with_dict_error_message_and_false_bool(
            self):
        self.requisition_id = None
        result = nordigen.validate_requisition(self.requisition_id)

        self.assertEqual(tuple, type(result))
        self.assertDictEqual({'message': 'Nordigen requisition key was not provided'}, result[0])
        self.assertFalse(result[1])

    def test_validate_requisition__when_requisition_id_is_invalid__expect_tuple_with_dict_error_message_and_false_bool(
            self):
        self.requisition_id = 'invalid_id'
        result = nordigen.validate_requisition(self.requisition_id)

        self.assertEqual(tuple, type(result))
        self.assertDictEqual({'detail': 'Not found.', 'status_code': 404}, result[0])
        self.assertFalse(result[1])

    def test_validate_requisition__when_requisition_id_is_valid__expect_tuple_with_requisition_data_and_true_bool(self):
        result = nordigen.validate_requisition(self.requisition_id)

        expected_requisition_data = {
            "id": "c0ad1b3e-28e1-4628-b8b1-f6009df3c27f",
            "created": "2021-10-06T22:21:31.216413Z",
            "redirect": "https://metiotube.herokuapp.com",
            "status": "LN",
            "agreements": [
                "f658eddc-2c4b-4f53-8c0d-1fb1995f327c"
            ],
            "accounts": [
                "1048f194-cb13-4cee-a55c-5ef6d8661341",
                "582a6ea9-81c7-4def-952d-85709d9432cf"
            ],
            "reference": "test",
            "enduser_id": "test"
        }

        self.assertDictEqual(expected_requisition_data, result[0])
        self.assertTrue(result[1])

    def test_get_bank_accounts__when_invalid_requisition_id__expect_tuple_with_dict_error_message_and_false_bool(self):
        self.requisition_id = 'invalid_id'
        result = nordigen.get_bank_accounts(self.requisition_id)

        self.assertEqual(tuple, type(result))
        self.assertDictEqual({'detail': 'Not found.', 'status_code': 404}, result[0])
        self.assertFalse(result[1])

    def test_get_bank_accounts__when_requisition_has_no_accounts__expect_tuple_with_dict_error_message_and_false_bool(
            self):
        self.requisition_id = '24dce3cb-f404-447e-8b0e-1c7c52e79810'
        result = nordigen.get_bank_accounts(self.requisition_id)

        self.assertEqual(tuple, type(result))
        self.assertDictEqual({'message': 'No bank accounts'}, result[0])
        self.assertFalse(result[1])

    def test_get_bank_accounts__when_requisition_has_accounts__expect_tuple_with_list_of_account_ids_and_true_bool(
            self):
        result = nordigen.get_bank_accounts(self.requisition_id)

        self.assertEqual(tuple, type(result))
        expected_result = ["1048f194-cb13-4cee-a55c-5ef6d8661341", "582a6ea9-81c7-4def-952d-85709d9432cf"]
        self.assertListEqual(expected_result, result[0])
        self.assertTrue(result[1])

    def test_get_account_balances__when_invalid_requisition_id__expect_dict_error_message(self):
        self.requisition_id = 'invalid_id'
        result = nordigen.get_account_balances(self.requisition_id)
        expected_result = {'detail': 'Not found.', 'status_code': 404}
        self.assertDictEqual(expected_result, result)

    def test_get_account_balances__when_valid_requisition_but_no_bank_accounts__expect_dict_error_message(self):
        self.requisition_id = '24dce3cb-f404-447e-8b0e-1c7c52e79810'
        result = nordigen.get_account_balances(self.requisition_id)
        expected_result = {'message': 'No bank accounts'}
        self.assertDictEqual(expected_result, result)

    def test_get_account_balances__when_valid_args__expect_dict_with_all_accounts_authorised_balances(self):
        result = nordigen.get_account_balances(self.requisition_id)
        expected_result = {
            "1048f194-cb13-4cee-a55c-5ef6d8661341": {
                "balanceAmount": {
                    "amount": "1913.12",
                    "currency": "EUR"
                },
                "balanceType": "authorised",
                "referenceDate": "2021-10-06"
            },
            "582a6ea9-81c7-4def-952d-85709d9432cf": {
                "balanceAmount": {
                    "amount": "1913.12",
                    "currency": "EUR"
                },
                "balanceType": "authorised",
                "referenceDate": "2021-10-06"
            }
        }

        self.assertDictEqual(expected_result, result)

    def test_get_account_transactions__when_invalid_requisition_id__expect_dict_error_message(self):
        self.requisition_id = 'invalid_id'
        result = nordigen.get_account_transactions(self.requisition_id)
        expected_result = {'detail': 'Not found.', 'status_code': 404}
        self.assertDictEqual(expected_result, result)

    def test_get_account_transactions__when_valid_requisition_but_no_bank_accounts__expect_dict_error_message(self):
        self.requisition_id = '24dce3cb-f404-447e-8b0e-1c7c52e79810'
        result = nordigen.get_account_transactions(self.requisition_id)
        expected_result = {'message': 'No bank accounts'}
        self.assertDictEqual(expected_result, result)

    def test_get_account_transactions__when_valid_args__expect_transactions_for_all_accounts(self):
        result = nordigen.get_account_transactions(self.requisition_id)
        self.assertEqual(2, len(result))
