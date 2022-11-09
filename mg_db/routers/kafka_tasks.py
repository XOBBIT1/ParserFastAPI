import json
from mg_db.config.mongo_db import loop, KAFKA_TOPIC, KAFKA_BOOTSRAP_SERVERS
from mg_db.models.clothe import Message
from fastapi import APIRouter
from aiokafka import AIOKafkaProducer

router_kafka = APIRouter()


@router_kafka.post("/create_message")
async def send(message: Message):
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSRAP_SERVERS)
    await producer.start()
    try:
        print(f"Sending message with value: {message}")
        value_jason = json.dumps(message.__dict__).encode("utf-8")
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_jason)
    finally:
        await producer.stop()



