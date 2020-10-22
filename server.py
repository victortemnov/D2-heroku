import sentry_sdk
from bottle import Bottle, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

SENTRY_DSN = "https://d38b13cc54fe49a3869b0aa349af4184@o464474.ingest.sentry.io/5473342"

sentry_sdk.init(dsn=SENTRY_DSN, integrations=[BottleIntegration()])

app = Bottle()

@app.route("/")
def index():
    return HTTPResponse(status=200, body="append to ulr <b>/success</b> or <b>/fail</b>")

@app.route("/success")
def success():
    return HTTPResponse(status=200, body="Success")

@app.route("/fail")
def fail():
    raise RuntimeError("Server error!")

if os.environ.get('SERVER_URL') == 'https://heroku-d2-hw.herokuapp.com':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
else:
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
