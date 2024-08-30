import time, logging, string, random

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("    ")

MONGOBD = os.getenv('MONGODB_URI')

def get_timestamp():
    return int(time.time())


def generate_unique_id(length=4):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for i in range(length))
