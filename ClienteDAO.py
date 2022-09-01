from fastapi import APIRouter
from pydantic import BaseModel


class Cliente(BaseModel):
    codigo: int = None
    nome: str
    cpf: str
    telefone: str = None
    compraFiado: bool
    diaFiado: int
    senha: str = None


router = APIRouter()
# Criar os endpoints de Cliente: GET, POST, PUT, DELETE


@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
    return {"msg": "get executado"}, 200


@router.post("/cliente/{id}", tags=["cliente"])
def post_cliente(id: int, c: Cliente):
    return {"msg": "post executado", "id": id, "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compraFiado": c.compraFiado, "diaFiado": c.diaFiado}, 200


@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, c: Cliente):
    return {"msg": "put executado", "id": id, "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compraFiado": c.compraFiado, "diaFiado": c.diaFiado}, 201


@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201
