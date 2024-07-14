from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1,2)
    @task
    def __index__(self):
        response = self.client.get("http://servidor_1:5000/")