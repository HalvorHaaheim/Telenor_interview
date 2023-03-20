import os
import uuid
import random
import pydantic
from typing import Optional
from redis.client import Redis
from constants import environments, customers, rule_names
from typing import List


class Event(pydantic.BaseModel):
    event_id: str
    rule_name: str
    customer_id: str
    env: str

# Changed to List[Event] from list[Event] here


def add_events_to_redis(events: List[Event]):
    client = Redis(host="localhost", port=5000, password="super-secret")

    for event in events:
        client.lpush("events", event.event_id)
        client.set(name=event.event_id, value=event.json())


def clear_redis():
    client = Redis(host="localhost", port=5000, password="super-secret")
    client.flushdb()


def create_event(
        environment: Optional[str] = None,
        customer_id: Optional[str] = None,
        rule_name: Optional[str] = None,
):
    if environment is None:
        environment = random.choice(environments)

    if customer_id is None:
        customer_id = random.choice(customers)

    if rule_name is None:
        rule_name = random.choice(rule_names)

    event_id = str(uuid.uuid4())

    return Event(
        rule_name=rule_name,
        customer_id=customer_id,
        env=environment,
        event_id=event_id,
    )
