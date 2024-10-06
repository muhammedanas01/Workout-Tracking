import requests
import datetime
import os


API_KEY = os.environ.get("N_API_KEY")
NUTRONIX_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("NUTRONIX_APP_ID")

headers = {
    'x-app-id': APP_ID,
    'x-app-key':API_KEY,
}

GENDER = "male"
WEIGHT = 74
AGE = 24
HEIGHT = 160

exercise_text = input("Which exercise did you do? ")


parameters = {
    "query":exercise_text,
    "gender": GENDER,
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age": AGE  
}

responce = requests.post(NUTRONIX_END_POINT, json=parameters, headers=headers)
result = responce.json()
print(result)

##############################################
sheet_end_point = os.environ.get("SHEET_END_POINT")

today_date = datetime.date.today()
date_str = today_date.strftime("%Y-%m-%d")

today_time = datetime.datetime.now().time()
time_str = today_time.strftime("%H:%M:%S")

sheety_user_name = os.environ.get("SHEETY_USERNAME")
sheety_password = os.environ.get("SHEETY_PASSWORD")

token = os.environ.get("SHEETY_TOKEN")
"789456123"

bearer_headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
    }


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date":date_str,
            "time":time_str,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],  
        }
    }

    sheet_responce = requests.post(sheet_end_point,json=sheet_inputs,headers=bearer_headers)
                               
    print(sheet_responce.text)