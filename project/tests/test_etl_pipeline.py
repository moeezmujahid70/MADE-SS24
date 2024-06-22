import unittest
import os

from ..pipeline.extract import extract_fao_temperature_data, extract_world_bank_co2_data
from ..pipeline.utils import data_directory


class TestETLPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.fao_zip_url = 'https://bulks-faostat.fao.org/production/Environment_Temperature_change_E_All_Data.zip'
        cls.world_bank_zip_url = 'https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv'

    def test_fao_temperature_data_extraction(self):
        temperature_data = extract_fao_temperature_data(self.fao_zip_url)
        target_file = os.path.join(
            data_directory, 'Environment_Temperature_change_E_All_Data.csv')
        self.assertTrue(os.path.exists(target_file),
                        "FAO temperature data file does not exist")
        self.assertIsNotNone(
            temperature_data, "Failed to extract FAO temperature data")

    def test_world_bank_co2_data_extraction(self):
        co2_data = extract_world_bank_co2_data(self.world_bank_zip_url)
        target_file = os.path.join(
            data_directory, 'API_EN.ATM.CO2E.KT_DS2_en_csv_v2_360757.csv')
        self.assertTrue(os.path.exists(target_file),
                        "World Bank CO2 data file does not exist")
        self.assertIsNotNone(co2_data, "Failed to extract World Bank CO2 data")


if __name__ == '__main__':
    unittest.main()
