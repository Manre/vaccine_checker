import time
from datetime import datetime

import pytz
import requests
import urllib3

urllib3.disable_warnings()

WAIT_TIME_IN_MINUTES = 10
SITES = ["avchile", "metropolis", "santafe"]
DAYS = [13, 14]


def checker():
  for site in SITES:
    for day in DAYS:
      schedule_url = f"https://vacunas.glya.co/preguntaragenda?date=2021/09/{day}&cc={site}"
      print(f"Revisando el CC {site} para el día {day}...")

      response = requests.get(schedule_url, verify=False)
      schedules_from_response = response.json()
      
      for schedule in schedules_from_response:
        available_spots = schedule["cupos_libres"]
        schedule_description = schedule["texto"]
        if available_spots > 0:
          print(f"GOOOOOOO!!! Hay {available_spots} cupos disponibles en la franja: {schedule_description}")

      print(f"Terminé de revisar el CC {site} para el día {day}...")
      time.sleep(5)


def main():
    while True:
      now_in_bogota = datetime.now(pytz.timezone("America/Bogota")).strftime("%Y-%m-%d, %I:%M:%S %p")

      print(f"Checking... {now_in_bogota}")

      checker()

      print("======")

      time.sleep(WAIT_TIME_IN_MINUTES*60)


if __name__ == "__main__":
    main()

