import random
from constants import GLOBAL_SPIKE_THRESHOLD
from utils import (
    environments,
    rule_names,
    create_event,
    add_events_to_redis,
)


def create_global_spike():
    """Ensure there is a global spike on at least one customer for an environment. There
    may be ongoing spikes both local and global for other customers after this has been
    executed"""
    spike_environment = random.choice(environments)
    spike_rule = random.choice(rule_names)

    print("Global spike threshold is set to", GLOBAL_SPIKE_THRESHOLD)
    print(
        "Created global spike for rule {} on environment {}".format(
            spike_rule, spike_environment
        )
    )

    events = []

    for _ in range(GLOBAL_SPIKE_THRESHOLD + 5):
        events.append(
            create_event(
                rule_name=spike_rule,
                environment=spike_environment,
            )
        )

    for _ in range(100):
        events.append(create_event())

    add_events_to_redis(events=events)


create_global_spike()
