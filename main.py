from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import choice
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite requisições de qualquer lugar
    allow_methods=["*"], # Permite GET, POST, etc.
    allow_headers=["*"],
)

class Requisicao(BaseModel):
    jogada: str

@app.post('/jogar')
def mariana(dados:Requisicao ):

    jogadaUsuario = dados.jogada.lower()

    lista_opcoes = ['pedra' , 'papel' , 'tesoura']

    jogadaMaquina = choice(lista_opcoes)

    if jogadaUsuario == 'papel' and jogadaMaquina == 'pedra':
        return { "computador": "pedra", "resultado": "vitoria"}
    if jogadaUsuario == 'pedra' and jogadaMaquina == 'tesoura':
        return { "computador": "tesoura", "resultado": "vitoria"}
    if jogadaUsuario == 'tesoura' and jogadaMaquina == 'papel':
        return { "computador": "papel", "resultado": "vitoria"}
    
    if jogadaMaquina == 'papel' and jogadaUsuario == 'pedra':
        return { "computador": "papel", "resultado": "derrota"}
    if jogadaMaquina == 'pedra' and jogadaUsuario == 'tesoura':
        return { "computador": "tesoura", "resultado": "derrota"}
    if jogadaMaquina == 'tesoura' and jogadaUsuario == 'papel':
        return { "computador": "papel", "resultado": "derrota"}
    
    if jogadaUsuario == jogadaMaquina:
        return { 'computador': jogadaMaquina, 'resultado': 'empate'}
    
    return 'estranho'



    