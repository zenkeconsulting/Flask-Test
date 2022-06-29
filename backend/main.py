import os
from flask import Flask
from flask import render_template
from flask import request
from intuitlib.client import AuthClient
from intuitlib.exceptions import AuthClientError
from intuitlib.enums import Scopes
import jinja2
import pandas as pd
import pdfkit

app = Flask(__name__)

CLIENT_ID = 'ABStjvBKj2eegllsilrSNW9DrdiLk9WtmioH6crwD0KPc2DTKq'
CLIENT_SECRET = 'LBc1ufKDFHF9qBDfhcXPBoeGTrNHhdLW9ap0Ov4U'
REDIRECT_URI = 'https://lionfish-app-qua6t.ondigitalocean.app/callback'
ENVIRONMENT = 'sandbox'

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/health")
def health():
    return ('', 204)

@app.route("/testPDF")
def test_PDF():
    print ('test 1')
    interest_rates = [i*.01 for i in range(1,11)]
    initial_account_sizes = [100, 500, 20000, 50000]
    data_frames = []
    for interest_rate in interest_rates:
        df = {}
        for initial_account_size in initial_account_sizes:
            df['Account Size: ' + str(initial_account_size)] = [initial_account_size * (1 + interest_rate) ** year for year in range(1, 21)]
        df = pd.DataFrame(df)
        df.index.name = 'year'
        data_frames.append({'df':df,
            'interest_rate':interest_rate})


    templateLoader = jinja2.FileSystemLoader(searchpath="./backend/templates/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "testPDF.html"
    template = templateEnv.get_template(TEMPLATE_FILE)

    for d in data_frames:
        outputText = template.render(df=d['df'],
                interest_rate=d['interest_rate'])
        html_file = open('./backend/templates/' + str(int(d['interest_rate'] * 100)) + '.html', 'w', encoding='utf-8')
        html_file.write(outputText)
        html_file.close()

    return render_template("1.html")

@app.route("/displaytestPDF")
def display_test_PDF():
    return render_template("1.html")

@app.route("/makePDF")
def make_PDF():
    pdfkit.from_file('./backend/templates/1.html', './backend/templates/1.pdf')
    return render_template("1.html")


@app.route("/login")
def login():
    print(CLIENT_ID)
    print(CLIENT_SECRET)
    print(REDIRECT_URI)
    print(ENVIRONMENT)
    auth_client = AuthClient(
        CLIENT_ID, 
        CLIENT_SECRET, 
        REDIRECT_URI, 
        ENVIRONMENT,
    )
    print ('test 1')
    url = auth_client.get_authorization_url([Scopes.ACCOUNTING])
    print ('test 2')
    #request.session['state'] = auth_client.state_token
    print ('test 3')
    return {"redirect_url": url}
    #return url

@app.route("/callback")
def callback():
    print ('test 1')
    auth_client = AuthClient(
        CLIENT_ID, 
        CLIENT_SECRET, 
        REDIRECT_URI, 
        ENVIRONMENT, 
    )
    print ('test 2')
    code = request.args.get('code')
    print (code)
    state = request.args.get('state')
    print (state)
    realmId = request.args.get('realmId')
    print (realmId)
    print ('test 3')
    if code is None:
         return {"status": "no_auth_code"}
    print ('test 4')
    try:
        print ('test 5')
        auth_client.get_bearer_token(code, realm_id=realmId)
        print ('test 6')
    except AuthClientError as e:
        # just printing status_code here but it can be used for retry workflows, etc
        print(e.status_code)
        print(e.content)
        print(e.intuit_tid)
    except Exception as e:
        print(e)
    print ('test 7')
    return {"access_token": auth_client.access_token,
            "refresh_token": auth_client.refresh_token,
            "id_token": auth_client.id_token}

if __name__ == "__main__":
    app.run(host='0.0.0.0')