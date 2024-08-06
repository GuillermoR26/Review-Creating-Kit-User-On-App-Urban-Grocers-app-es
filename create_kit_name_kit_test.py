import sender_stand_request
import data

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud de creacion de kit
def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body

# Función de prueba positiva para parametro name
def positive_assert(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201

# Función de prueba negativa para parametro name
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#Prueba 1: El número permitido de caracteres(1)
def test_1_name_one_allowed_character_get_success_response():
    positive_assert("a")

#Prueba 2: El número permitido de caracteres(511)
def test_2_name_511_allowed_numbers_get_success_response():
    positive_assert(data.el_número_permitido_de_caracteres_511)

#Prueba 3: El número de caracteres es menor que la cantidad permitida(0):
def test_3_name_none_characters_get_error_response():
    negative_assert_code_400("")

#Prueba 4: El número de caracteres es mayor que la cantidad permitida(512):
def test_4_name_512_characters_get_error_response():
    negative_assert_code_400(data.el_número_permitido_de_caracteres_512)

#Prueba 5. Se permiten caracteres especiales("%#$%,",):
def test_5_name_special_characters_allowed_get_success_response():
    positive_assert(data.caracteres_especiales)

#Prueba 6: Se permiten espacios(A aaa):
def test_6_name_spaces_are_allowed_get_success_response():
    positive_assert("A aaa")

#Prueba 7: Se permiten números(123):
def test_7_name_numbers_allowed_get_success_response():
    positive_assert("123")

#Prueba 8: El parámetro no se pasa en la solicitud{}:
def test_8_name_request_empty_get_error_response():
    negative_assert_code_400()

#Prueba 9: Se ha pasado un tipo de parámetro diferente(número):
def test_9_name_different_type_get_error_response():
    negative_assert_code_400(123)