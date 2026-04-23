import os
import json
import requests
from setting import YANDEX_DISK_TOKEN

class YandexDiskService:
    URL = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self):
        self.headers = {'Authorization': f'OAuth {YANDEX_DISK_TOKEN}'}

    def _create_folder(self, path: str) -> bool:
        url = f"{self.URL}/resources"
        params = {'path': path}
        response = requests.put(url, headers=self.headers, params=params)
        return response.status_code in (200, 201, 409)

    def _get_upload_link(self, file_path: str) -> str:
        url = f"{self.URL}/resources/upload"
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()['href']

    def upload_file(self, local_file_path: str, remote_file_path: str):
        folder_path = os.path.dirname(remote_file_path)
        if folder_path:
            self._create_folder(folder_path)

        upload_url = self._get_upload_link(remote_file_path)

        with open(local_file_path, 'rb') as f:
            response = requests.put(upload_url, data=f)
            response.raise_for_status()