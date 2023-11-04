import time
from plyer import notification

def send_notification(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 10
                        )
if __name__=="__main__":
    title = "Virus Attack"
    message = "Please shutdown your pc."
    send_notification(title,message)
