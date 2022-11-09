import motor.motor_asyncio
import asyncio

MONGODB_URL = "mongodb://localhost:27017/"

KAFKA_BOOTSRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'kafka'
KAFKA_CONSUMER_GROUP = 'group-id'

loop = asyncio.get_event_loop()
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.python_db
