import requests


class GoetterdaemmerungAPIClient():
    def __init__(self, api_key: str, url: str, match_strategies:list[str]):
        self.name = "Goetterdaemmerung"
        self.url = url
        self.api_key = api_key
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        self.match_strategies = match_strategies

    def request(self, text):
        payload = {
            "text": text,
            "match_strategies": self.match_strategies
        }
        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            # response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Fehler beim API-Call: {e}")
            return None
