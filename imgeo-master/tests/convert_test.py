import unittest
import os
import csv
from bson import json_util
from upload import *


class conversionTest(unittest.TestCase):
    """TestCase for the API conversion module"""

    def setUp(self):
        self.data_upload_folder = "uploads"
        self.client = 'localhost'
        os.chdir("../convert")

    def csv2geojson_test(self):
        """ Testing that CSV correctly translates to GeoJSON """

        input_csv = self.data_input_folder + "Greater_London_Const_Region.csv"
        output_geojson = self.data_output_folder + \
            "Greater_London_Const_Region.csv.geojson"
        csv_to_geojson(input_csv, output_geojson)
        self.assertTrue(os.path.exists(output_geojson) == 1,
                        msg="Current working directory is: , {0}".format(os.getcwd()))
        num_lines = sum(1 for line in open(output_geojson))
        self.assertTrue(num_lines == 136195)
        self.assertTrue(validate_geojson_from_file(output_geojson))

    def tearDown(self):
        self.db["testcupcakes"].drop()
        self.db["testurlcupcakes"].drop()


if __name__ == '__main__':
    unittest.main()
