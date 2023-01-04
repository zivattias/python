import unittest
from textfile import CsvFile, JsonFile, TxtFile, TextFile


class TestTextfile(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.csv_1 = CsvFile('/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/csv_1.csv')
        cls.csv_2 = CsvFile('/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/csv_2.csv',
                            ';')
        cls.csv_3 = CsvFile('/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/csv_3.csv')

        cls.txt_1 = TxtFile('/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/txt_1.txt')
        cls.txt_2 = TxtFile('/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/txt_2.txt')

        cls.json_1 = JsonFile(
            '/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/json_1.json')
        cls.json_2 = JsonFile(
            '/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/json_2.json')

    def test_paths(self):
        self.assertTrue(self.csv_1)
        self.assertTrue(self.txt_1)
        self.assertTrue(self.json_1)
        with self.assertRaises(Exception):
            TextFile.__init__(self.csv_1, '/Users/username_or_email.csv')
            TextFile.__init__(self.csv_1, '/Users/username_or_email.exe')

    def test_extensions(self):
        self.assertIs(CsvFile._get_extension(self.csv_1), 'csv')
        self.assertIs(JsonFile._get_extension(self.json_1), 'json')
        self.assertIs(TxtFile._get_extension(self.txt_1), 'txt')

    def test_equal(self):
        self.assertEqual(self.csv_1, self.csv_2)
        self.assertEqual(self.txt_1, self.txt_2)
        self.assertNotEqual(self.txt_1, self.json_1)

    def test_add(self):
        self.assertTrue(self.csv_1 + self.csv_2)
        self.assertTrue(self.txt_1 + self.txt_2)
        with self.assertRaises(TypeError, msg="Objects of different types cannot be concatenated"):
            TextFile.__add__(self.csv_1, self.txt_1)

    def test_new_file_dir(self):
        self.assertEqual(CsvFile.get_combined_path(self.csv_1, self.csv_2),
                         "/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/csv_1_csv_2.csv")
        self.assertEqual(TxtFile.get_combined_path(self.txt_1, self.txt_2),
                         "/Users/ziv.attias/PycharmProjects/lessons/lesson10-hw/textfile/files_ex/txt_1_txt_2.txt")


if __name__ == "__main__":
    unittest.main()
