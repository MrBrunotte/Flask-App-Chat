import os                       # import os to have access to the environment variables
from datetime import datetime
from flask import Flask, redirect, render_template         # import Flask, redirect and render_template

app = Flask(__name__)           # initialize the new flask app
messages = []                   # create an empty list called messages


def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """Main page with instructions"""
    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


#app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
if __name__ == '__main__':
    # NEVER HAVE DEBUG=TRUE IN PRODUCTION OR WHEN SUBMITTING!!!
    app.run(debug=True)

# we tell the app to use Heroku config vars for IP and PORT, this is set in settings in the Heroku dashboard
# app.run(host=os.environ.get('IP'),
#            port=int(os.environ.get('PORT')),
#            debug=True)
