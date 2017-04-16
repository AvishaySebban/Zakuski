import falcon
from resources import Get_User, Add_User,Update_User,Delete_User

app = falcon.API()
app.add_route('/apis/get/users', Get_User())
app.add_route('/apis/add/user', Add_User())
app.add_route('/apis/update/user_id', Update_User())
app.add_route('/apis/delete/user_id', Delete_User())

