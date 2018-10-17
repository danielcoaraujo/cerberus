import requests
import json


def getToken():
	try:
		payload = {
			'login': 'xxx',
			'password': 'xxx',
			'service': 'PrePagoDigital',
			'grant_type': 'authorization_code'
		}

		r = requests.post("http://.../NovoGia/getToken", data=payload)
		response = json.loads(r.content)
		token = response['access_token']
		return token
	except Exception:
		print '\n*** It was not possible to get the token. ***\n'
		token = ''
		return token