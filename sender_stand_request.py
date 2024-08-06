import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)

def get_new_user_token():
    response = post_new_user(data.user_body)
    response_json = response.json()
    return response_json["authToken"]

def post_new_client_kit(kit_body):
    auth_token = get_new_user_token()
    authorization = data.headers
    authorization["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,  # Cuerpo de la solicitud
                         headers=authorization)  # Encabezado de la solicitud
