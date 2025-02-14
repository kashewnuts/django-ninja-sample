"""ローカルで立ち上げたエンドポイントに連続アクセスするスクリプト."""

import httpx

url = "http://127.0.0.1:8000/api/cache-test"
requests_per_second = 1
interval = 1 / requests_per_second


def send_requests(url: str):
    while True:
        response = httpx.get(url)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        # time.sleep(interval)


if __name__ == "__main__":
    send_requests(url)
