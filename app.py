import falcon
from resources import GetUser, AddUser,UpdateUser,DeleteUser

app = falcon.API()
app.add_route('/apis/get/users', GetUser())
app.add_route('/apis/add/user', AddUser())
app.add_route('/apis/update/user_id', UpdateUser())
app.add_route('/apis/delete/user_id', DeleteUser())

