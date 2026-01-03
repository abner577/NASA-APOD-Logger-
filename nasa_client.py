import requests
import os
from dotenv import load_dotenv
import datetime
import json

load_dotenv()

NASA_API_KEY = os.getenv('NASA_API_KEY')
BASE_URL = os.getenv('BASE_URL')
NASA_APOD_START_DATE = datetime.date(1995, 6, 16)


def get_todays_apod():
    print("Getting today's apod...")

    full_url = f"{BASE_URL}?api_key={NASA_API_KEY}"
    response = requests.get(full_url)

    # We dont know how the data is formatted yet so maybe we can make a function to format data and return it
    # For now we can just leave a placeholder
    if response.status_code == 200:
        print("Today's apod was successfully retrieved! 🚀")
        apod_data = response.json()
        format_apod_data(apod_data)
        return apod_data

    elif response.status_code == 404 or response.status_code == 403:
        print("This is a user error. Check your API key and try again.")
        return None
    elif response.status_code == 500 or response.status_code == 503 or response.status_code == 504:
        print("This is a server error. Try again later.")
        return None

    return None


def format_apod_data(apod_data):
    return None


def get_apod_for_specific_day():
    flag = True
    while flag:
        try:
            print("================== GET APOD MENU 🛰️==================")
            year = int(input("Enter a year (YYYY): "))
            month = int(input("Enter a month (MM): "))
            day = int(input("Enter a day (DD): "))

            date_object = datetime.date(year, month, day)
            date_today = datetime.date.today()

            if date_object < NASA_APOD_START_DATE:
                print("⚠️ Please enter a date after June 16, 1995")
                print(flag)
            elif date_object > date_today:
                print(f"⚠️ Please enter a date before {date_today}")
            else:
                full_url = f"{BASE_URL}?api_key={NASA_API_KEY}&date={date_object}"
                print(full_url)
                print(date_object)
                print(f"Retrieving {date_object}'s APOD...")
                response = requests.get(full_url)
                print(response)

                if response.status_code == 200:
                    print("Today's apod was successfully retrieved! 🚀")
                    apod_data = response.json()
                    format_apod_data(apod_data)
                    flag = False
                    return apod_data

                elif response.status_code == 404 or response.status_code == 403:
                    print("🚫 This is a user error. Check your API key and try again.")
                elif response.status_code == 500 or response.status_code == 503 or response.status_code == 504:
                    print("⚠️ This is a server error. Try again later.")

        except Exception as e:
            print(e)
    return None
