from locust import HttpUser, task, between
from locust.exception import StopUser
from tests_api_performance.common import register_user_class


@register_user_class("matcher")
class MatcherUser(HttpUser):
    api_name = "matcher_api"
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

        if response.status_code != 200:
            raise RuntimeError(
                f"Matcher login fehlgeschlagen: {response.status_code} {response.text}"
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

    @task(3)
    def running_tasks(self):
        self.client.get(
            "/task/running",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/running",
        )

    @task(3)
    def history(self):
        self.client.get(
            "/task/history",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/history",
        )

    @task(2)
    def get_history_detail(self):
        response = self.client.get(
            "/task/history",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/history",
        )

        if response.status_code != 200:
            return

        try:
            runs = response.json()
        except Exception:
            return

        if not runs:
            return

        run_id = runs[0]["id"]

        self.client.get(
            f"/task/history/{run_id}",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/history/{{run_id}}",
        )

    @task(4)
    def matches(self):
        self.client.get(
            "/matches/",
            headers=self.auth_headers,
            name=f"{self.api_name}: /matches/",
        )

    @task(2)
    def get_match_detail(self):
        response = self.client.get(
            "/matches/",
            headers=self.auth_headers,
            name=f"{self.api_name}: /matches/ (for id lookup)",
        )

        if response.status_code != 200:
            return

        try:
            matches = response.json()
        except Exception:
            return

        if not matches:
            return

        match_id = matches[0]["id"]

        self.client.get(
            f"/matches/{match_id}",
            headers=self.auth_headers,
            name=f"{self.api_name}: /matches/{{id}}",
        )

    @task(1)
    def start_matcher(self):
        self.client.post(
            "/task/start",
            headers=self.auth_headers,
            json={
                "assets": [],
                "csaf_documents": [],
                "force_recompute": False,
            },
            name=f"{self.api_name}: /task/start",
        )

    @task(1)
    def stop_matcher(self):
        self.client.post(
            "/task/stop",
            headers=self.auth_headers,
            name=f"{self.api_name}: /task/stop",
        )
