import unittest
from pig import ui
from unittest.mock import patch


class TestPigUI(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input')
    def test_get_positive_int_input_without_min_value_specified(self, mock_input, mock_print):

        # Called without min_val. User should be able to enter 0, 1, 2.... 1000 but not -1, -100, sdfsdf, 6.7, -223.443,
        question = 'whatever'

        example_valid_data = ['4', '233423423', '0', '2']
        for data in example_valid_data:
            mock_input.return_value = data
            self.assertEqual(int(data), ui.positive_int_input(question))


        # Called with invalid data.
        valid = '0'

        mock_input.side_effect = ['-1', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question))

        mock_input.side_effect = ['hello', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question))

        mock_input.side_effect = ['34.43', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question))

        mock_input.side_effect = ['', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question))

        mock_input.side_effect = ['hello', '-1', '-100', '2334sdfwr', 'q123', '', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question))


        #TODO : could test for appropriate error message, use mock_print

    @patch('builtins.print')
    @patch('builtins.input')
    def test_get_positive_int_input_with_min_val(self, mock_input, mock_print):

        question = 'whatever'

        min_val = 4

        example_valid_data = ['4', '233423423', '10', '5']
        for data in example_valid_data:
            mock_input.return_value = data
            self.assertEqual(int(data), ui.positive_int_input(question, min_val))


        # Called with invalid data.
        valid = '5'

        # Smaller than minval
        mock_input.side_effect = ['0', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['3', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['-1', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['hello', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['34.43', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))

        mock_input.side_effect = ['hello', '-1', '0', '3' '-100', '2334sdfwr', 'q123', '', valid]  # Provide a valid value so function returns
        self.assertEqual(int(valid), ui.positive_int_input(question, min_val))




    @patch('builtins.input')
    def test_get_unique_names(self, mock_input):

        # test with 3 unique names
        mock_input.side_effect = ['a', 'b', 'c']
        names = ui.get_unique_names(3, 'whatever')
        self.assertEqual(names, ['a', 'b', 'c'])

        # test with a duplicate name - the second 'a' should be rejected
        mock_input.side_effect = ['a', 'b', 'a', 'c']
        names = ui.get_unique_names(3, 'whatever')
        self.assertEqual(names, ['a', 'b', 'c'])


        # test with several duplicate name - all the extra 'a' and 'c' should be rejected
        mock_input.side_effect = ['a', 'a', 'a', 'c', 'b', 'c', 'a', 'c']
        names = ui.get_unique_names(3, 'whatever')
        self.assertEqual(names, ['a', 'c', 'b'])




if __name__ == '__main__':
    unittest.main()
