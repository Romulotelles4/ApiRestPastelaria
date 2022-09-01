from fastapi import APIRouter
from pydantic import BaseModel


class Produto(BaseModel):
    codigo: int = None
    nome: str
    descricao: str
    foto: bytes
    valorUnitario: float


router = APIRouter()
# Criar os endpoints de produto: GET, POST, PUT, DELETE


@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    return {"msg": "get executado"}, 200


@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int, p: Produto):
    return {"msg": "post executado", "id": id, "nome": p.nome, "descricao": p.descricao, "foto": p.foto, "valorUnitario": p.valorUnitario}, 200


@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, p: Produto):
    return {"msg": "put executado", "id": id, "nome": p.nome, "descricao": p.descricao, "foto": p.foto, "valorUnitario": p.valorUnitario}, 201


@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201
