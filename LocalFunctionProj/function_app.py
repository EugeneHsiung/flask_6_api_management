import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="home")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('name', 'World')
    lastname = req.params.get('lastname', 'no last name provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()

    response = {
        "message": f'Hello {nameCapital} {lastnameCapital}!'
    }

    return func.HttpResponse(
        json.dumps(response),
        status_code=200
        )
# type in: /api/home?name=John&lastname=Smith (example)
# https://7071-cs-340668953872-default.cs-us-east1-vpcf.cloudshell.dev/api/home?
