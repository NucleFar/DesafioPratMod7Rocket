from .notificator_interface import NotificatorInterface

class NotificatorEmail(NotificatorInterface):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")