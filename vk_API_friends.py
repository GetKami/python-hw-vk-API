import requests
from urllib.parse import urlencode

APP_ID = 6779256
auth_url = "https://oauth.vk.com/authorize?"
user_id = 360342640

class Users_id():
    def __init__(self, user_1, user_2):
        self.user_1 = user_1
        self.user_2 = user_2

    def friends_1(self):
        users_list_1 = []
        params = {
            "access_token": "a79be4e2a79be4e2a79be4e2e1a7fc959aaa79ba79be4e2fb94e2dbeafbaeaae43d0b96",
            "user_id": self.user_1,
            "v": '5.92',
        }

        user_friends = requests.get("https://api.vk.com/method/friends.get?", params).json()
        for values in user_friends.values():
            for value in values.values():
                if type(value) == list:
                    users_list_1.extend(value)
        return users_list_1

    def friends_2(self):
        users_list_2 = []
        params = {
            "access_token": "a79be4e2a79be4e2a79be4e2e1a7fc959aaa79ba79be4e2fb94e2dbeafbaeaae43d0b96",
            "user_id": self.user_2,
            "v": "5.92",
        }

        user_friends = requests.get("https://api.vk.com/method/friends.get?", params).json()
        for values in user_friends.values():
            for value in values.values():
                if type(value) == list:
                    users_list_2.extend(value)
        return users_list_2

    def common_friends(self):
        user_1_friends = set(self.user_1.friends_1())
        user_2_friends = set(self.user_2.friends_2())
        mutual_list = user_1_friends & user_2_friends
        print(mutual_list, len(mutual_list))

    def get_link(self):
        user_link = "https://vk.com/id" + str(self.user_id)
        return user_link

friends = Users_id(360342640, 30904863)
print(friends.common_friends())