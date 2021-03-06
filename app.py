from flask import Flask
from views import *

# Configure flask app name
app = Flask(__name__, template_folder="templates")

# Configure app route
app.add_url_rule('/', 'home', index)
app.add_url_rule('/contact-us', 'contact', contact_us)
app.add_url_rule('/about', 'about', about)
app.add_url_rule('/hello', 'hello', say_hello)
app.add_url_rule('/sum/', 'sum', sum_func, defaults={'number1': 10, 'number2': 12})
app.add_url_rule('/sum/<int:number1>+<int:number2>', 'sum', sum_func)
app.add_url_rule('/power/<int:number1>/', 'power', power_func, defaults={'number2': 2})
app.add_url_rule('/power/<int:number1>/<int:number2>', 'power', power_func)
app.add_url_rule('/r/<path:link>', 'redirecter', redirect_func)
app.add_url_rule('/printer/<text>', 'printer', printer_func, methods=['GET', 'POST'])
app.add_url_rule('/request_info/', 'request_info', requests_func)
# app.add_url_rule('/users', 'users', users, methods=['GET', 'POST'])
# app.add_url_rule('/users/<int:user_id>', 'get_user', get_user)
app.add_url_rule('/posts', 'posts', post_list)
app.add_url_rule('/post/<int:post_id>', 'post_detail_view', post_detail)
app.add_url_rule('/create/', 'new_post', create_post, methods=['GET', 'POST'])

# user;
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run()
