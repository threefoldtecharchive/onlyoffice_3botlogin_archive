import threebotlogin
from onlyoffice import OnlyOfficeAuthenticator
from config import config
from flask import Flask, request, redirect, session

app = Flask(__name__)

threebotlogin.configure(app, config['threebot-appid'], config['threebot-privatekey'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


