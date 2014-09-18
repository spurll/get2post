import os


CSRF_ENABLED = True
SECRET_KEY = os.urandom(30)
PROPAGATE_EXCEPTIONS = True

PORT = 9995

# Externally Accessible
HOST = "0.0.0.0"
SERVER_NAME = "savage.startleddisbelief.com:{}".format(PORT)

