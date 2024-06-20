import unittest
import os
import pandas as pd
import sqlite3
from pipeline.load import save_to_csv, merge_datasets, save_to_sqlite
from pipeline.utils import get_directory_absolute_path


class TestLoad(unittest.TestCase):

    def setUp(self):
        # Set up data for testing
        self.temp_data = pd.DataFrame({
            'Area': ['Country1', 'Country2'],
            'Year': [1961, 1962],
            'Change': [0.5, 0.6]
        })

        self.co2_data = pd.DataFrame({
            'Area': ['Country1', 'Country2'],
            'Year': [1961, 1962],
            'co2_emissions': [123.4, 234.5]
        })

        self.test_csv_file = 'test_output.csv'
        self.test_db_name = 'test_db'
        self.test_table_name = 'test_table'
        self.cwd = get_directory_absolute_path()
        self.test_db_path = f"{self.cwd}/data/{self.test_db_name}.sqlite"

    def tearDown(self):
        # Clean up any temp files created during the tests
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)

    def test_save_to_csv(self):
        '''test if CSV files were created'''
        save_to_csv(self.temp_data, self.test_csv_file)
        self.assertTrue(os.path.exists(self.test_csv_file),
                        "CSV file was not created")

    def test_merge_datasets(self):
        '''testing merged datasets'''
        merged_df = merge_datasets(self.temp_data, self.co2_data)
        self.assertIsNotNone(merged_df, "Merged DataFrame is None")
        self.assertEqual(
            len(merged_df), 2, "Merged DataFrame does not have the expected number of rows")
        self.assertIn('co2_emissions', merged_df.columns,
                      "Merged DataFrame does not contain 'co2_emissions' column")

    def test_save_to_sqlite(self):
        '''tests if files were successfully saved to DB'''
        save_to_sqlite(self.temp_data, self.test_db_name, self.test_table_name)
        conn = sqlite3.connect(self.test_db_path)
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.test_table_name}';"
        result = conn.execute(query).fetchone()
        conn.close()
        self.assertIsNotNone(
            result, "Table was not created in SQLite database")


if __name__ == '__main__':
    unittest.main()
