from django.core.management.base import BaseCommand
from update.models import SaveUpdateNotification
import requests
import subprocess

class Command(BaseCommand):
    help = 'Updates home devices'

    def handle(self, *args, **options):
        response = requests.get("http://127.0.0.1:9000/update/download-file/")  # get update from cloud
        print('Cloud Response:', response.json())
        subprocess.run(['fab', 'partially_update'])
        latest_update = SaveUpdateNotification.objects.last().version
        print('latest version: ', latest_update)
        response = requests.get("http://127.0.0.1:8000/update/status/home", params={'version': latest_update})  # send error to fog
        print('Fog Response:', response.json(), response.status_code)
        if response.status_code != 200:
            subprocess.run(['fab', 'restore_update'])  
            print('Code restored') # restore code
        elif response.status_code == 200:
            print('New updates applied')  # update exists on fog... update all files
        else:
            print('An error occured on fog server')