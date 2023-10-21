import json
import unittest


from models.user import User
from models.pet import Pet


class TaskTests(unittest.TestCase):

    def test_create_user(self):
        response = User().create_user()
        assert response.status_code == 200

    def test_create_users_list(self):
        response = User().create_users_list()
        assert response.status_code == 200

    def test_user_login(self):
        response = User().user_login()
        assert response.status_code == 200
        self.assertIn('logged in user session', response.text)


    def test_create_pet(self):
        response = Pet().add_new_pet()
        assert response.status_code == 200

    def test_update_pet_image(self):
        response = Pet().update_pet_image(45, "new_image")
        assert response.status_code == 200
        print(response.json().get("photoUrls"))

    def test_update_pet_name_status(self):
        response = Pet().update_pet_name_status(45, "New_name", "unavailable")
        assert response.status_code == 200
        print(response.json().get("name"), response.json().get("status"))

    def test_delete_pet(self):
        response = Pet().delete_pet(45)
        assert response.status_code == 200

    def test_user_logout(self):
        response = User().user_logout()
        assert response.status_code == 200






if __name__ == "__main__":
    unittest.main()
