import unittest
import requests


class TestYandexDiskAPI(unittest.TestCase):

    def test_create_folder_negative(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": "Bearer INVALID_TOKEN",
            "Content-Type": "application/json"
        }
        params = {
            "path": "/NewFolder"
        }
        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 401)

    def test_create_folder_invalid_path(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }
        params = {
            "path": "/&%^InvalidPath"
        }
        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
