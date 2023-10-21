from core.base_controller import BaseController
from data.pet_data import PetData
import requests


class Pet(BaseController):
    endpoint_pet = '/pet'

    def add_new_pet(self):
        return requests.post(BaseController.base_url + self.endpoint_pet, json=PetData().get_valid_pet(),
                             headers=BaseController.headers)

    def update_pet_image(self, pet_id, image_url):
        payload = {
            "id": pet_id,
            "photoUrls": [image_url]
        }
        return requests.put(BaseController.base_url + self.endpoint_pet, json=payload, headers=BaseController.headers)

    def update_pet_name_status(self, pet_id, new_name, new_status):
        payload = {
            "id": pet_id,
            "name": new_name,
            "status": new_status
        }
        return requests.put(BaseController.base_url + self.endpoint_pet, json=payload, headers=BaseController.headers)

    def delete_pet(self, pet_id):
        return requests.delete(BaseController.base_url + self.endpoint_pet + "/" + str(pet_id),
                               headers=BaseController.headers)
