class UserAuthorizationValidator:
    def __init__(self,authorized_users_list:list):
        self.authorized_users = authorized_users_list
    
    def is_user_authorized(self, username:str):
        return username in self.authorized_users

