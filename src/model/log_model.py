class LogModel:
    def __init__(self, hostname, ip, created_at, log_text):
        self.hostname = hostname
        self.ip = ip
        self.created_at = str(created_at)
        self.log_text = log_text

    def to_string(self):
        return "-" + "|" + self.hostname + "|" + self.ip + "|" + self.created_at + "|" + self.log_text