import pytest
from app.app import app

@pytest.fixture()
def client():
    app.config.update({"TESTING": True})
    with app.test_client() as c:
        yield c

def test_operacion_no_valida(client):
    r = client.post("/", data={"num1": "1", "num2": "2", "operacion": "potenciar"})
    assert r.status_code == 200
    assert b"Operaci\xc3\xb3n no v\xc3\xa1lida" in r.data  # "Operación no válida"

def test_valor_invalido_num1(client):
    r = client.post("/", data={"num1": "x", "num2": "2", "operacion": "sumar"})
    assert r.status_code == 200
    assert "Introduce números válidos" in r.data.decode("utf-8")

def test_valor_invalido_num2(client):
    r = client.post("/", data={"num1": "2", "num2": "y", "operacion": "sumar"})
    assert r.status_code == 200
    assert "Introduce números válidos" in r.data.decode("utf-8")

def test_division_por_cero(client):
    r = client.post("/", data={"num1": "1", "num2": "0", "operacion": "dividir"})
    assert r.status_code == 200
    assert b"No se puede dividir por cero" in r.data
