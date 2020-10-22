import sentry_sdk
import os
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

SENTRY_DSN = "https://d38b13cc54fe49a3869b0aa349af4184@o464474.ingest.sentry.io/5473342"

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[BottleIntegration()]
)

@route("/")
def index():
    return HTTPResponse(status=200, body="append to url /success or /fail")

@route("/success")
def sucess():
    return HTTPResponse(status=200, body="OK")

@route("/fail")
def fail():
    raise RuntimeError("Server error")


if __name__ == "__main__":

    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
    
