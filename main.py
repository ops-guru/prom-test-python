#!/usr/bin/python3

from prometheus_client import start_http_server, Summary, Counter, Gauge

import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

c = Counter('custom_counter', 'Some custom counter')
c.inc()     # Increment by 1

g = Gauge('my_inprogress_requests', 'Gauge: unixtime')
g.set_to_current_time()   # Set to current unixtime

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8001)
    # Generate some requests.
    while True:
        process_request(random.random())
        g.set_to_current_time()   # Set to current unixtime


