import time, logging, string, random, os

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("    ")

MONGODB = "mongodb+srv://daramolacpe186651:T8vhI4cfu8zyDddO@cluster0.maqru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def get_timestamp():
    return int(time.time())


def generate_unique_id(length=4):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for i in range(length))
