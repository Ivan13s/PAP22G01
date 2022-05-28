import json
import unittest
from file2 import time_getter
from unittest.mock import patch, MagicMock

output=['Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Helsinki', 'Europe/Istanbul', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Oslo', 'Europe/Paris', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zaporozhye', 'Europe/Zurich']

class TestTimetGetter(unittest.TestCase):
    @patch('c14_linters_and_unitest.file2.requests.get')
    def test_response(self, get_mock:MagicMock):
        get_mock.return_value=MagicMock(text=json.dumps(output))
        self.assertEqual(time_getter('Europe'),output)
    @patch('c14_linters_and_unitest.file2.requests.get')
    def test_response_2(self, get_mock:MagicMock):
        get_mock.return_value=json.dumps(output)
        self.assertEqual(time_getter('Europe'),output)

if __name__=='__main__':
    unittest.main()