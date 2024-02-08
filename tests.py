from flask import Flask, request

#teste

app = Flask(__name__)

class SaveIPMiddleware:
    def __init__(self, app):
        self.app = app
        self.client_ip = None

    def __call__(self, environ, start_response):
        self.client_ip = environ.get('REMOTE_ADDR', 'IP Desconhecido')
        return self.app(environ, start_response)

app.wsgi_app = SaveIPMiddleware(app.wsgi_app)

if __name__ == "__main__":
    print(f"IP do cliente ao iniciar a aplicação: {app.wsgi_app.client_ip}")
    app.run(debug=True)
