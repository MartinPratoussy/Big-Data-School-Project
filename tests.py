import unittest
import os
import json

import constants

class TestStringMethods(unittest.TestCase):

    def test_imports(self):
        self.assertNotEqual(len(os.listdir(constants.RESSOURCES_FOLDER)), 0)

    def test_image_analysis(self):
        #file exists
        self.assertTrue(os.path.isfile(f"{constants.DATA_FOLDER}{constants.ANALYZED_DATA}"))

        with open(f'{constants.DATA_FOLDER}{constants.ANALYZED_DATA}') as json_file:
            json_decoded = json.load(json_file)

        #json not empty
        self.assertNotEqual(json_decoded, "")

    def test_favorites(self):
        #file exists
        self.assertTrue(os.path.isfile(f"{constants.DATA_FOLDER}{constants.FAVORITES_DATA}"))

        with open(f'{constants.DATA_FOLDER}{constants.FAVORITES_DATA}') as json_file:
            json_decoded = json.load(json_file)

        #json not empty
        self.assertNotEqual(json_decoded, "")

    def test_recommended(self):
        #file exists
        self.assertTrue(os.path.isfile(f"{constants.DATA_FOLDER}{constants.RECOMMENDED_DATA}"))

        with open(f'{constants.DATA_FOLDER}{constants.RECOMMENDED_DATA}') as json_file:
            json_decoded = json.load(json_file)

        #json not empty
        self.assertNotEqual(json_decoded, "")

if __name__ == '__main__':
    unittest.main()