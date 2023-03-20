import redis
import time
import json
import queue
import threading
from typing import *
from constants import *
from utils import (
    environments,
    rule_names,
    create_event,
    add_events_to_redis,
    clear_redis,
)

# Connect to redis
r = redis.Redis(host="localhost", port=5000, password="super-secret")

# Setting local threshold
local_spike_threshold = 10

# Setting global threshold
global_spike_threshold = 20

# Create a list to hold events that will be kept
events_to_keep = []

# Retrieve all events from Redis and add them to a queue
events_queue = r.lrange('events', 0, -1)

# Process events in the queue one by one
for event_str in events_queue:

    # Count the number of events for this rule, customer, and environment to check if there already are alot of the
    # same events
    num_local_events = 0
    num_global_events = 0

    # Create a new dictionary of the current event being processed by the string
    event_dict = r.get(event_str.decode('utf-8'))
    event_dict = json.loads(event_dict)

    # Making a loop to count spikes and notice anomalies
    for e in events_queue:
        if e == event_str:
            continue  # skip the current event being processed to stop duplicating checks
        e_dict = r.get(e.decode('utf-8'))
        e_dict = json.loads(e_dict)
        if e_dict.get('rule_name') == event_dict.get('rule_name') and e_dict.get('customer_id') == event_dict.get('customer_id') and e_dict.get('env') == event_dict.get('env'):
            num_local_events += 1
        if e_dict.get('rule_name') == event_dict.get('rule_name') and e_dict.get('env') == event_dict.get('env'):
            num_global_events += 1

    # Determine whether this event should be kept or discarded
    if num_local_events > local_spike_threshold:
        print(f"Discarding local spike event: {event_str}")
    elif num_global_events > global_spike_threshold:
        print(f"Discarding global spike event: {event_str}")
    else:
        events_to_keep.append(event_str)

# Remove all events from Redis
clear_redis()

# print("The following events will be kept: ")
# print(events_to_keep)
# Push the events to be kept back onto Redis
add_events_to_redis(events=events_to_keep)

