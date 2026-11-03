from locust import HttpUser, task, between
from locust.exception import StopUser
from tests_api_performance.common import register_user_class


@register_user_class("assetsync")
class AssetSyncUser(HttpUser):
    api_name = "assetsync_api"
    wait_time = between(1, 3)
    host = None

    def on_start(self):
        if self.host is None:
            raise StopUser("No host for matcher_api")

        response = self.client.post(
            "/token",
            data={"username": "admin", "password": "admin"},
            name=f"{self.api_name}: /token",
        )
        data = response.json()
        self.auth_headers = {"Authorization": f"Bearer {data['access_token']}"}

    @task(5)
    def status(self):
        self.client.get(
            "/task/status",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/status",
        )

    @task(1)
    def start_sync(self):
        self.client.post(
            "/task/start",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/start",
        )

    @task(1)
    def stop_sync(self):
        self.client.post(
            "/task/stop",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/stop",
        )
