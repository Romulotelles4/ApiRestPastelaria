from fastapi import APIRouter
from pydantic import BaseModel


class Funcionario(BaseModel):
    codigo: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None


router = APIRouter()
# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE


@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario(id: int):
    return {"msg": "get executado"}, 200


@router.post("/funcionario/{id}", tags=["funcionario"])
def post_funcionario(id: int, f: Funcionario):
    return {"msg": "post executado", "id": id, "nome": f.nome, "matricula": f.matricula, "cpf": f.cpf, "telefone": f.telefone, "grupo": f.grupo}, 200


@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int, f: Funcionario):
    return {"msg": "put executado", "id": id, "nome": f.nome, "matricula": f.matricula, "cpf": f.cpf, "telefone": f.telefone, "grupo": f.grupo}, 201


@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
    return {"msg": "delete executado"}, 201
