import os
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from bottle import run, route, HTTPResponse
from dotenv import load_dotenv
load_dotenv()


sentry_sdk.init(dsn=os.environ['SENTRY_DSN'], integrations=[BottleIntegration()])

@route("/")
def index():
    form = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>D2 Temnov</title>
        <style>
        
            body {
                background-color: black;
            }
        
            h1 {
                color: deeppink;
            }
            
            hr {
                color: magenta;
            }
            
            h2 {
                color: darkorchid;
            }
        
            span {
                color: red;
            }
            
        </style>
    </head>
    <body>
        <h1>This is main page</h1>
        <hr>
        <h2>For visit successful page, append to the end of URL "https://heroku-d2-hw.herokuapp.com<span>/success</span>"</h2>
        <hr>
        <h2>For visit fail page, append to the end of URL "https://heroku-d2-hw.herokuapp.com<span>/fail</span>"</h2>
        <hr>
    </body>
</html>
"""
    return form

@route("/success")
def sucess():
    return HTTPResponse(status=200, body="Successful page")

@route("/fail")
def fail():
    raise RuntimeError("Fail page")
    return HTTPResponse(status=500, body="Fail page")


if __name__ == "__main__":

    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
    
