import requests
import json



class Patients:
    def __init__(self, pid, type, value,reference):
        self.pid = pid
        self.type = type
        self.value = value
        self.ref = reference

    def __str__(self):
        return "pid:{}, type:{},value: {}".format(self.pid,self.type,self.value)


if __name__ == '__main__':
    # temp = []
    # with open('patients_observations.json','r') as f:
    #     file = f.read()
    #
    # patient_json = json.loads(file)
    # measure_type = set()
    # for item in patient_json:
    #     try:
    #         measure_type.add(item['resource']['code']['coding'][0]['display'])
    #     except IndexError:
    #         pass
    #
    # print(measure_type)

    OAuthurl = 'https://sandbox86.tactiorpm7000.com/token.php'
    APIurl = 'https://sandbox86.tactiorpm7000.com/tactio-clinician-api/1.1.4'

    # '''Authentication'''
    body = {
    "grant_type": "password",
    "client_id": "083e9a44a763473fbeb62fbf90b74551",
    "client_secret": "ba09798f0921456e8b4e5e4588ea536d",
    "username": "tactioClinician",
    "password": "tactio"
    }

    response = requests.post(OAuthurl, data=body)
    auth_code = response.json()["access_token"]


    # patient_info_raw = requests.get(APIurl+'/patient',headers={'Authorization':'Bearer token {}'.format()}) # put token in format()
    # patient_info_json = json.loads(patient_info_raw.text)
    # print(patient_info_json)

    # '''Observation '''
    '''
        Observation parameter search by code must be in tuple form. Other parameter search patterns can use dictionary
        Here is an example:
            observation_param = {"subject": "e5850a8f-5a21-49c5-80be-5270e3b126bb"}
    '''

    observation_param = [("code", "1742-6"),("code", "1742-6")]
    patient_observation_raw = requests.get(APIurl + '/Observation', headers={
        'Authorization': 'Bearer {}'.format(auth_code)},
                                           params=observation_param)  # put token here
    patient_obs_json = patient_observation_raw.json()
    print(patient_obs_json) # json as dictionary
    print(patient_obs_json['entry'][0]['resource']['code']['coding'][0]['display']) # how to access the measurement category. 0 for loinc, 1 for snomed
    '''
        open the json file in text editor and see how to retrieve a specific attribute.
    '''
    print(patient_obs_json['entry'][0]['resource']['valueQuantity'])
    patient_id_call = patient_obs_json['entry'][0]['resource']['subject']['reference']
    # pid = patient_id_call[8:]

    ''' Similar for patient personal information, using the patient observation, can get /patient[+id]. Just plug in the request here'''
    patient_param = {''}
    patient_info_raw = requests.get(APIurl+"/{}".format(patient_id_call), headers={
        'Authorization': 'Bearer {}'.format(auth_code)})
    print(patient_info_raw.json()['gender'])
    print(patient_info_raw.json()['birthDate'])
