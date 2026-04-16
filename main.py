import json
import os
from ip_service import IPService
from geo_service import GeoService
from yandex_disk_service import YandexDiskService
from config import FOLDER_NAME, JSON_FILE

def main():
    ip_service = IPService()
    geo_service = GeoService()
    yandex_service = YandexDiskService()

    temp_json_path = 'temp_geolocation.json'

    try:
        # Шаг 1: Получаем IP-адрес
        print("Получение IP-адреса...")
        ip = ip_service.get_ip()
        print(f"IP-адрес: {ip}")

        #  Получаем геоинформацию
        print("Получение геоинформации...")
        geolocation_data = geo_service.get_geolocation(ip)

        # Добавляем IP
        geolocation_data['ip'] = ip

        print("Сохранение данных в JSON...")
        with open(temp_json_path, 'w', encoding='utf-8') as f:
            json.dump(geolocation_data, f, ensure_ascii=False, indent=2)

        print("Загрузка файла на Яндекс.Диск...")
        remote_path = f"{FOLDER_NAME}/{JSON_FILE}"
        yandex_service.upload_file(temp_json_path, remote_path)
        print("Файл загружен на Яндекс.Диск!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise
    finally:
        # Удаляем временный файл
        if os.path.exists(temp_json_path):
            os.remove(temp_json_path)
            print("Временный файл удалён.")

if __name__ == '__main__':
    main()