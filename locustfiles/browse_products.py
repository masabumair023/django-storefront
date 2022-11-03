from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1,5)


    @task
    def view_product(self):
        product_id = randint(1,4)
        self.client.get(
            f'/store/products/{product_id}', 
            name='store/products/:id')

    @task
    def say_hello(self):
        self.client.get('/playground/hello/')