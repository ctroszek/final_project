from api.api_user import ApiUser


def test_user_api(api_setting):
    user_data = api_setting
    p_user = ApiUser()
    p_user.create_user(user_data)
    p_user.login_user(user_data['username'], user_data['password'])
    p_user.get_correct_user_data(user_data)
    p_user.user_logout()
    p_user.delete_user(user_data['username'])
