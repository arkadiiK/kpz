import requests


class TranslateAPI:
    @staticmethod
    def translate_to_minion(text):
        base_url = 'https://api.funtranslations.com/translate/minion.json'
        params = {"text": text}
        response = requests.post(base_url, data=params)
        if response.status_code == 200:
            return response.json()['contents']['translated']
        else:
            print('Error', response.status_code)
            return None



