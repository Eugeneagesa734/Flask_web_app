from flask import Flask


def create_app():
    app = (__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    return app
