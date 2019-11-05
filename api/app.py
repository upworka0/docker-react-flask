from flask import Flask, redirect, request
from client import ConstantClient, get_client
import json
from dotenv import load_dotenv
from pathlib import Path
import os


# load env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Define Constant Client and its credentials
CLIENT_ID = os.getenv("CLIENT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "contact_data+campaign_data"
RESPONSE_TYPE = "code"
SECRET = os.getenv("SECRET")


app = Flask(__name__)


@app.route('/')
def index():
    client = get_client(client_id=CLIENT_ID, secret=SECRET, redirect_uri=REDIRECT_URI,
                            scope=SCOPE, response_type=RESPONSE_TYPE)
    if client.token_loaded:
        return redirect('/contact_list')

    auth_url = client.generate_auth_url()
    print("Auth Url:", auth_url)
    return redirect(auth_url)


@app.route('/oauth/redirect')
def get_code():
    client = get_client(client_id=CLIENT_ID, secret=SECRET, redirect_uri=REDIRECT_URI,
                        scope=SCOPE, response_type=RESPONSE_TYPE)
    code = request.args.get('code')
    client.get_tokens(code=code)
    if client.token_loaded:
        return redirect('/contact_list')


@app.route('/contact_list')
def contact_list():
    """Show contact lists"""

    #bJnLIM4IhJbNrdJYeojJjatuBhFA
    #ouOXMZAArBobj4FA078EPPi9elZd4ieyNAEm6meQjj

    client = get_client(client_id=CLIENT_ID, secret=SECRET, redirect_uri=REDIRECT_URI,
                        scope=SCOPE, response_type=RESPONSE_TYPE)

    if not client.token_loaded:
        return redirect('/')

    res = client.get_contact_list()
    return json.dumps(res)


@app.route('/campaigns')
def campaigns():
    """Show contact lists"""

    #bJnLIM4IhJbNrdJYeojJjatuBhFA
    #ouOXMZAArBobj4FA078EPPi9elZd4ieyNAEm6meQjj

    client = get_client(client_id=CLIENT_ID, secret=SECRET, redirect_uri=REDIRECT_URI,
                        scope=SCOPE, response_type=RESPONSE_TYPE)

    if not client.token_loaded:
        return redirect('/')

    res = client.get_campaigns()
    return json.dumps(res)


if __name__=='__main__':
    app.run(debug=True)