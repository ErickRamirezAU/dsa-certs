
from pprint import pprint    # for pretty formatting
import requests              # for making REST API requests
import json                  # for converting json payloads to strings
import uuid                  # to create UUIDs for Astra connections
import os                    # for accessing creds
from flask import render_template, request, redirect, url_for, abort



from flask import Flask
app = Flask(__name__)

# set up stuff

class Client:
    """
    An API Client for connecting to Stargate
    """

    def __init__(self, base_url, access_token, headers):
        self.base_url = base_url
        self.access_token = access_token
        self.headers = headers

    def post(self, payload={}, path=""):
        """
            Via the requests library, performs a post with the payload to the path
        """
        return requests.post(self.base_url + path,
                             data=json.dumps(payload),
                             headers=self.headers)

    def put(self, payload={}, path=""):
        """
            Via the requests library, performs a put with the payload to the path
        """
        return requests.put(self.base_url + path,
                            data=json.dumps(payload),
                            headers=self.headers)

    def patch(self, payload={}, path=""):
        """
            Via the requests library, performs a patch with the payload to the path
        """
        return requests.patch(self.base_url + path,
                              data=json.dumps(payload),
                              headers=self.headers)

    def get(self, payload={}, path=""):
        """
            Via the requests library, performs a get with the payload to the path
        """
        return requests.get(self.base_url + path,
                            data=json.dumps(payload),
                            headers=self.headers)

    def delete(self, payload={}, path=""):
        """
            Via the requests library, performs a delete with the payload to the path
        """
        return requests.delete(self.base_url + path,
                               data=json.dumps(payload),
                               headers=self.headers)

UUID = str(uuid.uuid1())
USER = os.environ["ASTRA_DB_USERNAME"]     # NEVER store your creds directly in your code!
PASSWORD = os.environ["ASTRA_DB_PASSWORD"] # NEVER store your creds directly in your code!
DB_ID = os.environ["ASTRA_DB_ID"]          # NEVER store your creds directly in your code!
REGION = os.environ["ASTRA_DB_REGION"]     # NEVER store your creds directly in your code!
BASE_URL = f"https://{DB_ID}-{REGION}.apps.astra.datastax.com"

def authenticate(path="/api/rest/v1/auth"):
    """
        This convenience function uses the v1 auth REST API to get an access token
        returns: an auth token; 30 minute expiration
    """
    url = BASE_URL + path # we still have to auth with the v1 API
    payload = {"username": USER,
               "password": PASSWORD}
    headers = {'accept': '*/*',
               'content-type': 'application/json',
               'x-cassandra-request-id': UUID}
    # make auth request to Astra
    r = requests.post(url,
                      data=json.dumps(payload),
                      headers=headers)
    # raise any authentication errror
    if r.status_code != 200:
        raise Exception(r.text)
    # extract and return the auth token
    data = json.loads(r.text)
    return data["authToken"]

TOKEN = authenticate()
print(TOKEN)
HEADERS = {'content-type': 'application/json',
           'x-cassandra-token': TOKEN}
stargate_client = Client(BASE_URL, TOKEN, HEADERS)


# keyspace, doc root etc
KEYSPACE = "stargate"
TABLE = "users_by_last_name"
DOC_ROOT_PATH = f"/api/rest/v2/keyspaces/{KEYSPACE}/{TABLE}/"



@app.route('/hello/', methods=["GET"])
def welcome():
    name = "welcome"
    return redirect(url_for('hello', name=name))


@app.route('/hello/<name>')
def hello(name):
    if not name:
        name = ""
    response = stargate_client.get(
        {}, DOC_ROOT_PATH + name
    )
    data=json.loads(response.text)
    name_data = data["data"]
    return render_template('hello.html', name_data=name_data)


@app.route('/find_by_name/<name>')
def get_certificates(name):
    response = stargate_client.get(
        {}, DOC_ROOT_PATH + name
    )
    data = json.loads(response.text)
    if len(data) == 0:
        abort(404)
    if data["count"] == 0:
        return ("no data for this name")
    return redirect(url_for('hello', name=name))



