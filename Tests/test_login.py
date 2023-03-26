import unittest
import login


class TestFunctions(unittest.TestCase):

    def test_split_data(self):

        expected = ["Sidumiso", "sidumisodebbie@gmail.com"]
        result = login.info_split("Sidumiso - sidumisodebbie@gmail.com")

        self.assertEqual(expected, result)
        self.assertTrue(list, type(result))

    def test_user_data(self):

        expected = {'Sidumiso': 'sidumisodebbie@gmail.com'}
        result = login.user_info(["Sidumiso - sidumisodebbie@gmail.com\n"])

        self.assertEqual(expected, result)
        self.assertTrue(dict, type(result))


if __name__ == "__main__":

    unittest.main()