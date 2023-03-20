import random
from constants import GLOBAL_SPIKE_THRESHOLD, EVENT_LIMIT
from utils import (
    environments,
    rule_names,
    create_event,
    add_events_to_redis,
)


def add_events():
    """Add events to the queue, there are no guarantees as to whether this will trigger
    a spike or not"""
    print(f"Added {EVENT_LIMIT} events to Redis")

    events = []

    for _ in range(int(EVENT_LIMIT)):
        events.append(create_event())

    add_events_to_redis(events=events)


add_events()
