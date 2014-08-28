import os


basedir = os.path.abspath(os.path.dirname(__file__))

PORT = 9995

# Local Testing
TEST_HOST = "127.0.0.1"     # Must be 0.0.0.0 for external availability.
TEST_SERVER_NAME = "localhost:{}".format(PORT)

# Externally Accessible
HOST = "0.0.0.0"            # Must be 0.0.0.0 for external availability.
SERVER_NAME = "savage.startleddisbelief.com:{}".format(PORT)

CSRF_ENABLED = True
SECRET_KEY = os.urandom(30)

