import unittest
import pandas as pd
from pipeline.trasform import transform_temperature_data, transform_co2_data


class TestTransform(unittest.TestCase):

    def setUp(self):
        # Set up the raw data
        self.raw_temperature_data = pd.DataFrame({
            'Area': ['Country1', 'Country2'],
            'Element': ['Temperature change', 'Temperature change'],
            'Area Code': [1, 2],
            'Area Code (M49)': [100, 400],
            'Element Code': [7020, 7040],
            'Months': ['January', 'February'],
            'Months Code': [7010, 7011],
            'Unit': ['Celsius', 'Celsius'],
            'Y1961': [0.9, 0.6],
            'Y1961F': ['E', 'E'],
            'Y1962': [0.4, 0.7],
            'Y1962F': ['E', 'E'],

        })

        self.raw_co2_data = pd.DataFrame({
            'Country Name': ['Coun1', 'Coun2'],
            'Country Code': ['C01', 'C02'],
            'Indicator Name': ['CO2 emissions', 'CO2 emissions'],
            'Indicator Code': ['EN.ATM.CO2E.KT', 'EN.ATM.CO2E.KT'],
            '1960': [123.4, 234.5],
            '1961': [345.6, 456.7],

        })

    def test_transform_co2_data(self):
        transformed_co2_data = transform_co2_data(self.raw_co2_data)
        self.assertIsNotNone(transformed_co2_data,
                             "Failed to transform CO2 data")
        self.assertIn('co2_emissions', transformed_co2_data.columns,
                      "Transformed CO2 data does not contain 'co2_emissions' column")
        self.assertIn('Year', transformed_co2_data.columns,
                      "Transformed CO2 data does not contain 'Year' column")
        self.assertIn('Area', transformed_co2_data.columns,
                      "Transformed CO2 data does not contain 'Area' column")

    def test_transform_temperature_data(self):
        transformed_temp_data = transform_temperature_data(
            self.raw_temperature_data)
        self.assertIsNotNone(transformed_temp_data,
                             "Failed to transform temperature data")
        self.assertIn('Change', transformed_temp_data.columns,
                      "Transformed temperature data does not contain 'Change' column")
        self.assertIn('Year', transformed_temp_data.columns,
                      "Transformed temperature data does not contain 'Year' column")
        self.assertIn('Area', transformed_temp_data.columns,
                      "Transformed temperature data does not contain 'Area' column")


if __name__ == '__main__':
    unittest.main()
