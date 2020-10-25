import os
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from bottle import run, route, HTTPResponse
from dotenv import load_dotenv
load_dotenv()


sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[BottleIntegration()]
)

@route("/")
def index():
    return HTTPResponse(status=200, body="Nothing bad happend. Append to URL '/success' or '/fail'")

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
    
