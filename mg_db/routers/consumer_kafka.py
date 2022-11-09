from fastapi_back.backend import app
from mg_db.config.mongo_db import loop, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC, KAFKA_BOOTSRAP_SERVERS
from aiokafka import AIOKafkaConsumer


@app.on_event("startup")
async def consumer_lamoda():
    await consumer_kafka()


async def consumer_kafka():
    consumer_kafka = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop, bootstrap_servers=KAFKA_BOOTSRAP_SERVERS,
                                      group_id=KAFKA_CONSUMER_GROUP)
    await consumer_kafka.start()
    try:
        async for msg in consumer_kafka:
            print(f"Consumer msg:{msg}")
            await msg
    finally:
        await consumer_kafka.stop()
