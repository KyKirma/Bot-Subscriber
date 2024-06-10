import requests

data = {'email': 'saler.kourly@gmail.com', 
        'publickey': '30444372', 
        'apikey': 'ac4351df11e342466ae44d9c7f30de73cb9723a2273b633f129a96d44bdda6e5'}

response = requests.post('https://api2.eduzz.com/credential/generate_token', data = data)
info = response.json()
token = info['data']['token']
headers = {"Token": f"{token}"}

response = requests.get('https://api2.eduzz.com/subscription/get_contract_list', headers=headers)
subsList = response.json()

for data in subsList['data']:
    print(data)
    clientName = data['client_name']
    clientEmail = data['client_email']

    print(f'Nome do cliente: {clientName}\n' + 
            f'Email do cliente: {clientEmail}') 
