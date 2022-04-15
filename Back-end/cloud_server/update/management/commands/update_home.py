from django.core.management.base import BaseCommand
import requests
import subprocess

class Command(BaseCommand):
    help = 'Updates home devices'

    def handle(self, *args, **options):
        response = requests.get("http://127.0.0.1:7000/update/device-update/")
        print('Home Response:', response.json())
        if response.status_code == 200:
            print('New updates applied')  # update exists on fog... update all files
        else:
            print('An error occured on home server')