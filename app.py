from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("Accessed root endpoint")
    return "Hello from Cloud Run!"

@app.route('/checkout')
def checkout():
    app.logger.info("Simulating checkout")
    return "Checkout complete!"