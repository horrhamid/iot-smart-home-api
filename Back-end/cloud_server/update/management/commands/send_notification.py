from django.core.management.base import BaseCommand
import requests
from django.conf import settings


class Command(BaseCommand):
    help = 'Send New Update Notification to IOT server'

    def handle(self, *args, **options):
        iot_url = settings.IOT_SERVER_BASE_URL + 'update/receive-update-notification'
        rsp = requests.get(iot_url)
        print(f'Response: {rsp.text}, status code: {rsp.status_code}')

