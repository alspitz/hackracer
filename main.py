import random
from flask import Flask, url_for, render_template, request
from challenge import challenges
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/', methods=["GET", "POST"])
def hello():
  if request.method == "POST":
    challenge_id = int(request.form['id'])
    challenge_code = request.form['code']
    challenge = challenges[challenge_id]
    errors = challenge.get_errors(challenge_code)
    if errors:
      return errors

    if challenges[challenge_id].check(challenge_code):
      return "Correct!"
    else:
      return "Incorrect."

  else:
    challenge_id = random.randint(0, len(challenges)-1)
    return render_template('test.html', \
                           challenge_prompt=challenges[challenge_id].text, \
                           challenge_id=challenge_id)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
