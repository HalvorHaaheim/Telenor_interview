import random
from constants import LOCAL_SPIKE_THRESHOLD
from utils import (
    environments,
    customers,
    rule_names,
    create_event,
    add_events_to_redis,
)


def create_local_spike():
    """Ensure there is a local spike on at least one customer. There may be ongoing
    spikes both local and global for other customers after this has been executed"""
    spike_environment = random.choice(environments)
    spike_customer = random.choice(customers)
    spike_rule = random.choice(rule_names)

    print("Global spike threshold is set to", LOCAL_SPIKE_THRESHOLD)
    print(
        "Created local spike for rule {} on environment {} for customer {}".format(
            spike_rule, spike_environment, spike_customer
        )
    )

    events = []

    for _ in range(LOCAL_SPIKE_THRESHOLD + 5):
        events.append(
            create_event(
                rule_name=spike_rule,
                customer_id=spike_customer,
                environment=spike_environment,
            )
        )

    for _ in range(100):
        events.append(create_event())

    add_events_to_redis(events=events)


create_local_spike()
