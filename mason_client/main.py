import time

import tell_stats_to_server


if __name__ == "__main__":
    while True:
        time.sleep(10)
        tell_stats_to_server.tell()