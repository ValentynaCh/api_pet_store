from core.base_controller import BaseController
from data.user_data import UserData
import requests


class User(BaseController):
    endpoint_user: str = '/user'
    endpoint_array_of_users = '/user/createWithArray'
    endpoint_login = '/user/login'
    endpoint_logout = '/user/logout'

    def create_user(self):
        return requests.post(BaseController.base_url + self.endpoint_user, json=UserData().get_valid_user(), headers= BaseController.headers)

    def create_users_list(self):
        return requests.post(BaseController.base_url + self.endpoint_array_of_users, json=UserData().get_valid_users_list(),
                      headers=BaseController.headers)

    def user_login(self):
        return requests.get(BaseController.base_url + self.endpoint_login, params=UserData().get_user_credentials())


    def user_logout(self):
        return requests.get(BaseController.base_url + self.endpoint_logout)





