import requests


class ApiUser:

    def get_headers(self):
        headers = {
            'Accept': 'application/json'
        }
        return headers

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2/user'
        self.headers = self.get_headers()

    def create_user(self, user_data):
        url = self.base_url
        json = user_data
        answer = requests.request("POST", url, json=json)
        json_response = answer.json()
        assert json_response['code'] == 200, \
            f'{json_response["code"]} not equal code 200'
        print('created')
        return json_response

    def login_user(self, username, password):
        url = self.base_url + '/login'
        params = {
            "username": username,
            "password": password
        }

        answer = requests.request("GET", url, params=params,
                                  headers=self.headers)
        json_response = answer.json()
        assert json_response['code'] == 200, \
            f'{json_response["code"]} ERROR'
        print('created')
        return json_response

    def get_correct_user_data(self, user_data):
        url = self.base_url + f"/{user_data['username']}"
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        print(json_response)
        print(user_data)
        assert json_response == user_data, f'{json_response} invalid user_data'
        print('data')
        return json_response

    def user_logout(self):
        url = self.base_url + '/logout'
        response = requests.request("GET", url, headers=self.headers)
        json_response = response.json()
        assert json_response['code'] == 200 and \
               f'{json_response["code"]} ERROR'
        print('logout')
        return json_response

    def delete_user(self, username):
        url = self.base_url + f'/{username}'
        response = requests.request("DELETE", url, headers=self.headers)
        json_response = response.json()
        assert json_response['code'] == 200,\
            f'{json_response["code"]} ERROR'
        print('deleted')
        return json_response
