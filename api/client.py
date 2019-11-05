from urllib.parse import urlparse, parse_qs, urlencode
import requests
import os
import base64
from pprint import pprint

GET = 1
POST = 2
PUT = 3
DELETE = 4

SUCCESS = 5
INVALUD_TOKEN = 6
UNKNOW = 7


class ConstantClient:
    """ ConstantContact rest api wrapper
        """
    AUTH_URL = "https://api.cc.email/v3/idfed"
    TOKEN_URL = "https://idfed.constantcontact.com/as/token.oauth2"
    BASE_URL = "https://api.cc.email/v3"

    access_token = None
    refresh_token = None
    file_name = "tokens.txt"
    token_loaded = False

    def __init__(self, client_id, secret, redirect_uri, scope, response_type):
        self.client_id = client_id
        self.redirct_uri = redirect_uri
        self.scope = scope
        self.secret = secret
        self.response_type = response_type
        self.token_loaded = self.load_tokens()
        if self.access_token and not self.validate_token():
            self.update_access_token()

    def _request(self, url, method=GET, params={}):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.access_token,
            'Cache-Control': 'no-cache'
        }

        if method == GET:
            res = requests.get(url, headers=headers)
        elif method == POST:
            res =  requests.post(url, data=params, headers=headers)
        elif method == PUT:
            res = requests.post(url, data=params, headers=headers)
        elif method == DELETE:
            res = requests.delete(url)

        return res


    def generate_auth_url(self):
        """ Generate auth request url with parmas including clientid, redirect_uri, scope
            """
        parmas = {
            "client_id": self.client_id,
            "redirect_uri": self.redirct_uri,
            "response_type": self.response_type,
            "scope": self.scope
        }

        auth_url = "%s?%s" %(self.AUTH_URL, urlencode(parmas))
        return auth_url

    def load_tokens(self):
        """
            Load access and refresh tokens from file
            """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as f:
                tokens = f.readlines()
                if len(tokens)>1:
                    self.access_token = tokens[0].strip()
                    self.refresh_token = tokens[1].strip()
                    return True
            f.close()
        return False

    def validate_token(self):
        """ Check the access token validation
            """
        url = "%s/contacts/test" % (self.BASE_URL)
        res = self._request(url)
        if res.status_code == 401:
            return False
        return True

    def store_tokens(self):
        """ Store access and refresh tokens to file
            """
        with open(self.file_name, 'w') as f:
            f.write(self.access_token + '\n')
            f.write(self.refresh_token + '\n')
        f.close()
        self.token_loaded = True

    def get_tokens(self, code):
        """ Get access_token and refresh_token with code
            """
        params = {
            "code": code,
            "redirect_uri": self.redirct_uri,
            "grant_type": "authorization_code"
        }

        auth = "%s:%s" % (self.client_id, self.secret)
        headers = {
            "Authorization": "Basic %s" % base64.b64encode(auth.encode('ascii')).decode('utf-8')
        }

        res = requests.post(self.TOKEN_URL, data=params, headers=headers)
        print("------- Get Tokens using Code ---------")
        pprint(res.json())
        res = res.json()
        if 'access_token' in res:
            self.access_token = res['access_token']
            self.refresh_token = res['refresh_token']
            self.store_tokens()

    def update_access_token(self):
        """ Update access_token with refresh_token
            """
        params = {
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }

        auth = "%s:%s" % (self.client_id, self.secret)
        headers = {
            "Authorization": "Basic %s" % base64.b64encode(auth.encode('ascii')).decode('utf-8')
        }

        res = requests.post(self.TOKEN_URL, data=params, headers=headers)
        print("------- Get Tokens using RefreshToken ---------")
        pprint(res.json())
        res = res.json()
        if 'access_token' in res:
            self.access_token = res['access_token']
            self.refresh_token = res['refresh_token']
            self.store_tokens()
        else:
            self.token_loaded = False
            raise Exception('Invalid Refresh Token. Remove tokens in tokens.txt file and try again')

    def check_response(self, response):
        """ Check the response status
            """
        if response.status_code < 400:
            return SUCCESS

        if response.status_code == 401:
            return INVALUD_TOKEN

        return UNKNOW

    def get_contact_list(self):
        """ Get contacts list
            """
        url = "%s/contact_lists" % self.BASE_URL
        res = self._request(url)
        return res.json()

    def get_contact(self, contact_id):
        """ Get Contact by id
            """
        url = "%s/contacts/%s" % (self.BASE_URL, contact_id)
        res = self._request(url)
        return res.json()

    def get_campaigns(self):
        """ Get all Campaigns
            """
        url = "%s/emails" % self.BASE_URL
        res = self._request(url)
        return res.json()



def get_client(client_id, secret, redirect_uri, scope, response_type):
    client = ConstantClient(client_id=client_id, secret=secret, redirect_uri=redirect_uri,
                            scope=scope, response_type=response_type)
    return client
