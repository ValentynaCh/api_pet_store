class UserData:
    def get_valid_user(self):
        return {
            "id": 12396845,
            "username": "testuser",
            "firstName": "John",
            "lastName": "Doe",
            "email": "testuser@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 2
        }

    def get_valid_users_list(self):
        return [{"id": 12985,
                 "username": "testuser2",
                 "firstName": "David",
                 "lastName": "Smith",
                 "email": "testuserdav@example.com",
                 "password": "password123",
                 "phone": "1234565590",
                 "userStatus": 2
                 }, {
                    "id": 12932,
                    "username": "testuser3",
                    "firstName": "Jorge",
                    "lastName": "Pitt",
                    "email": "testuserdav@example.com",
                    "password": "password123",
                    "phone": "1234567890",
                    "userStatus": 3
                }]

    def get_user_credentials(self):
        return {
            "username": "testuser3",
            "password": "password123"
        }
