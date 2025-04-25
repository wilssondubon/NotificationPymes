import json
import sys
import os

# Agregar la ruta del módulo al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/handlers')))

from send_notification import handler

def test_lambda_handler():
    event = {
        'name': 'Alice'
    }
    response = handler(event, None)
    assert response['statusCode'] == 200
    assert response['body'] == '"Notificacion enviada (aun no implementado)"'

def test_lambda_handler_default():
    event = {}
    response = handler(event, None)
    assert response['statusCode'] == 200
    assert response['body'] == '"Notificacion enviada (aun no implementado"'