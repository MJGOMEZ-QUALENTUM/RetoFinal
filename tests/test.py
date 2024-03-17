import unittest
import requests
import random

class TestApp(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000"
        # Limpiar la base de datos antes de cada prueba
        requests.delete(f"{self.base_url}/data")

    def test_insert_data(self):
        # Generar un nombre aleatorio para la inserción de datos
        random_name = f"Insercion{random.randint(1, 100)}"

        # Realizar una solicitud POST para insertar datos con el nombre aleatorio
        data = {"name": random_name}
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/data", json=data, headers=headers)
        
        # Verificar que la inserción fue exitosa
        self.assertEqual(response.status_code, 200)  

    def test_get_data(self):
        # Realizar una solicitud GET para obtener los datos
        response = requests.get(f"{self.base_url}/data")

        # Verificar que la solicitud fue exitosa
        self.assertEqual(response.status_code, 200)  

        # Verificar que la respuesta contiene datos
        data = response.json()
        self.assertTrue(data)  # Verificar que la lista de datos no está vacía

    def test_invalid_route(self):
        # Realizar una solicitud GET a una ruta inexistente
        response = requests.get(f"{self.base_url}/invalid_route")
        self.assertEqual(response.status_code, 404)

    def test_invalid_method(self):
        # Realizar una solicitud POST a una ruta que solo permite GET
        response = requests.post(f"{self.base_url}/data")
        self.assertEqual(response.status_code, 415)
    
    def test_insert_data_response(self):
        random_name = f"Insercion{random.randint(1, 100)}"
        data = {"name": random_name}
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/data", json=data, headers=headers)

        # Verificar que la respuesta contiene un mensaje de éxito
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Data inserted successfully")
    
    def test_insert_duplicate_data(self):
        # Insertar datos duplicados
        random_name = f"Duplicado{random.randint(1, 100)}"
        data = {"name": random_name}
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}/data", json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

        # Intentar insertar los mismos datos nuevamente
        response = requests.post(f"{self.base_url}/data", json=data, headers=headers)
        
        # Verificar que se recibe un código de estado 409 (conflicto)
        self.assertEqual(response.status_code, 409)