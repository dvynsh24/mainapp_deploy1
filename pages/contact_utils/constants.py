import os
# import environ
from dotenv import load_dotenv
# from os.path import join, dirname, abspath


load_dotenv()

# env = environ.Env()

# env.read_env(
#     env.str("ENV_PATH", join(dirname(dirname(abspath(__file__))), ".env"))
# )

SMTP_SERVER_ADDRESS = os.environ["SMTP_SERVER_ADDRESS"]
SENDER_ADDRESS = os.environ["SENDER_ADDRESS"]
SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
PORT = os.environ["PORT"]
