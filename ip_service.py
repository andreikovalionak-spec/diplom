import requests

class IPService:

    def __init__(self, ipify_url='https://api.ipify.org'):
        self.ipify_url = ipify_url

    def get_ip(self) -> str:
        try:
            response = requests.get(self.ipify_url)
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            raise ConnectionError(f"Ошибка при получении IP-адреса: {e}")