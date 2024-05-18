# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, Blueprint, session, redirect, render_template
from app.routes.admin import bp_admin
from app.models.admin import User
from app.helpers import login_required

main = Blueprint("main", __name__)

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello Mr %s!' % name


def create_app():
   app = Flask(__name__)
   
   app.register_blueprint(main)
   app.register_blueprint(bp_admin, url_prefix='/admin')

   return app

@main.route("/")
@main.route("/index")
@login_required
def index():
   print(" >>> Index - session = ", session)

   if int(User.Role.ADMIN.value) in session['role']:
      return redirect("/admin")
   else:
      return redirect("/orders")
    
@main.route("/login", methods=["GET", "POST"])
def login():
   session.clear()
   return render_template("login.html")


# main driver function
if __name__ == '__main__':
    
    app = create_app()

    app.run(debug=True)

