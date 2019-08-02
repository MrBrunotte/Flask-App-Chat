import os                       # import os to have access to the environment variables
from datetime import datetime
# import Flask, redirect and render_template
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)           # initialize the new flask app
app.secret_key = "randomstring123"
messages = []                   # create an empty list called messages


def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}

    messages.append(messages_dict)

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return render_template("chat.html", username = username, chat_messages = messages)

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
