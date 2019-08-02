import os                       # import os to have access to the environment variables
from flask import Flask         # import Flask

app = Flask(__name__)           # initialize the new flask app


@app.route('/')                 # create the app route decorator.
# define the function  that is going to bound to our decorator.
def index():
    """ Main page instructions """
    return "To send a message /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    return "Hi " + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username,message)

#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


if __name__ == '__main__':
    # NEVER HAVE DEBUG=TRUE IN PRODUCTION OR WHEN SUBMITTING!!!
    app.run(debug=True)

# we tell the app to use Heroku config vars for IP and PORT, this is set in settings in the Heroku dashboard
# app.run(host=os.environ.get('IP'),
#            port=int(os.environ.get('PORT')),
#            debug=True)
