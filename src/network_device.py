import logging


class NetworkDevice:
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

    def summarize(self):
        summary = f"{self.hostname} ({self.type}) - {self.ip}"
        print(summary)
        logging.info(f"DEVICE_SUMMARY: {summary}")
        return summary