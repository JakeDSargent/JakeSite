from flask import Flask
from flaskr import create_app

app = create_app()

app.run(host='0.0.0.0', port=81)