from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Modelo de dados
class Produto(BaseModel):
    id: int
    nome: str
    preco: float

class DescontoRequest(BaseModel):
    percentual: float

# Banco de dados simulado
produtos_db = [
    {"id": 1, "nome": "Notebook", "preco": 3000.00},
    {"id": 2, "nome": "Mouse", "preco": 50.00},
    {"id": 3, "nome": "Teclado", "preco": 150.00},
]

# Endpoints
@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API de Produtos"}

@app.get("/produtos")
def listar_produtos():
    return {"produtos": produtos_db}

@app.get("/produtos/{produto_id}")
def consultar_produto(produto_id: int):
    produto = next((p for p in produtos_db if p["id"] == produto_id), None)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos/{produto_id}/desconto")
def aplicar_desconto(produto_id: int, desconto: DescontoRequest):
    produto = next((p for p in produtos_db if p["id"] == produto_id), None)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if desconto.percentual < 0 or desconto.percentual > 100:
        raise HTTPException(status_code=400, detail="Percentual deve estar entre 0 e 100")
    
    preco_original = produto["preco"]
    produto["preco"] = preco_original * (1 - desconto.percentual / 100)
    
    return {
        "id": produto["id"],
        "nome": produto["nome"],
        "preco_original": preco_original,
        "desconto_percentual": desconto.percentual,
        "preco_final": produto["preco"]
    }

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)