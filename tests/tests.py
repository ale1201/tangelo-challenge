import unittest
from unittest.mock import patch, Mock
import pandas as pd
import os
from main import countries_information
import json


class TestsCountries(unittest.TestCase):

    def test_countries_information(self):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"region": "America", "name": {"common": "Colombia"}, "languages": {"lang1": "Spanish, English"}},
            {"region": "Europe", "name": {"common": "Germany"}, "languages": {"lang2": "German"}},
            {"region": "Asia", "name": {"common": "China"}, "languages": {"lang2": "Chinese"}},
        ]

        mock_conn = Mock()
        sql_conn = Mock()

        with patch('requests.get', return_value=mock_response), \
                patch('sqlite3.connect', return_value=mock_conn), \
                patch('pandas.DataFrame.to_sql', return_value=sql_conn), \
                patch('hashlib.sha1') as mock_sha1:
            mock_sha1_instance = Mock()
            mock_sha1_instance.hexdigest.return_value = 'mocked_hash'
            mock_sha1.return_value = mock_sha1_instance

            df, stats_df = countries_information('urlmock.com', 'moch_database', 'json_files/tests.json')

        self.assertIsInstance(df, pd.DataFrame)

        self.assertEqual(len(df), 3)
        self.assertEqual(df['Region'][0], 'America')
        self.assertEqual(df['Region'][1], 'Europe')
        self.assertEqual(df['Region'][2], 'Asia')

        self.assertEqual(df['Country Name'][0], 'Colombia')
        self.assertEqual(df['Country Name'][1], 'Germany')
        self.assertEqual(df['Country Name'][2], 'China')

        self.assertIsInstance(stats_df, pd.DataFrame)
        self.assertEqual(len(stats_df), 8)
        self.assertEqual([elem for elem in stats_df.columns], ['Parameter', 'Value Time (ms)'])

        self.assertTrue(os.path.exists('json_files/tests.json'))

        with open('json_files/tests.json', 'r') as f:
            content = json.loads(f.read())

        json_file = {
            'time_stats': stats_df.to_dict(orient='records'),
            'countries': df.to_dict(orient='records'),
        }
        self.assertEqual(content, json_file)

    def test_print_hi_fail(self):
        mock_response = Mock()
        mock_response.status_code = 404

        mock_conn = Mock()

        sql_conn = Mock()

        with patch('requests.get', return_value=mock_response), \
                patch('sqlite3.connect', return_value=mock_conn), \
                patch('pandas.DataFrame.to_sql', return_value=sql_conn), \
                patch('hashlib.sha1') as mock_sha1:
            mock_sha1_instance = Mock()
            mock_sha1_instance.hexdigest.return_value = 'mocked_hash'
            mock_sha1.return_value = mock_sha1_instance

            with self.assertRaises(Exception):
                countries_information('urlmock.com', 'moch_database', 'json_files/tests.json')


if __name__ == '__main__':
    unittest.main()
