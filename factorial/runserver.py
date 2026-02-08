from os import environ
from factorial import app

if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST", "127.0.0.1")
    PORT = int(environ.get("SERVER_PORT", 5555))
    app.run(host=HOST, port=PORT, debug=True)