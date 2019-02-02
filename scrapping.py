import requests
import json

# OAuthurl = 'https://sandbox86.tactiorpm7000.com/token.php'
APIurl = 'https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4'

# body = {
# "grant_type": "password",
# "client_id": "083e9a44a763473fbeb62fbf90b74551",
# "client_secret": "ba09798f0921456e8b4e5e4588ea536d",
# "username": "tactioClinician",
# "password": "tactio"
# }
#
# response = requests.post(OAuthurl, data=body)




# json_data = json.loads(response.text)
# print(json_data)


patient_info_raw = requests.get(APIurl+'/patient',headers={'Authorization':'token {}'.format('1c6069aae80f38638ffb9c53dec6137ac99b5f4b')}) # put token here
patient_info_json = json.loads(patient_info_raw.text)
# print(patient_info_json)

patient_observation_raw = requests.get(APIurl+'/Observation',headers={'Authorization':'token {}'.format('1c6069aae80f38638ffb9c53dec6137ac99b5f4b')}) # put token here

#print(patient_observation_raw.text)

with open("/data_file.json", "r") as write_files:
    json.dump(patient_observation_raw.json(), write_files)
