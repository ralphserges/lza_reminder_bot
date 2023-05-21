import unittest
from validators import *

class TestUserAuthorizationValidator(unittest.TestCase):

    def test_is_user_authorized(self):
        mock_authorized_user_list = ['lebronjames','stephcurry']
        test_user_authorization_obj = UserAuthorizationValidator(mock_authorized_user_list)
        self.assertTrue(test_user_authorization_obj.is_user_authorized('lebronjames'))
        self.assertFalse(test_user_authorization_obj.is_user_authorized('stephhhhhh'))


class TestUserInputValidator(unittest.TestCase):

    def test_validate_new_reminder_input(self):
        todays_date = datetime.now().date().strftime(r'%Y-%m-%d')
        todays_time = datetime.now().time().strftime(r'%H%M')
        mock_username = 'mockuser123'
        mock_new_reminder_input = f'Add_reminder\nMy mother birthday\n{todays_date}\n{todays_time}\ntrue\nRmb to buy bird nest for her'

        test_user_input_validator = UserInputValidator()
        validation_result = test_user_input_validator.validate_new_reminder_input(mock_new_reminder_input,mock_username)

        self.assertEqual(validation_result.reminder_name, 'My mother birthday')
        self.assertEqual(validation_result.creator_name, mock_username)
        self.assertEqual(validation_result.date.strftime(r'%Y-%m-%d'), todays_date)
        self.assertEqual(validation_result.time.strftime(r'%H%M'), todays_time)
        self.assertEqual(validation_result.is_recurring, 'true')
        self.assertEqual(validation_result.reminder_description, 'Rmb to buy bird nest for her')