import requests

class GeoService:

    def __init__(self, ipinfo_base_url='https://ipinfo.io'):
        self.ipinfo_base_url = ipinfo_base_url

    def get_geolocation(self, ip: str) -> dict:
        url = f"{self.ipinfo_base_url}/{ip}/geo"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError(f"Ошибка при получении геоинформации: {e}")
