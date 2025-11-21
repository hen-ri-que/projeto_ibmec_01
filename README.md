# projeto_ibmec_01
Projeto para Avaliação da Disciplina de Engenharia de Software, Prof. Luis Fernando Lufe Mello Barreto - MBA/IBMEC
Estudantes: Henrique Pimentel, Felipe Gouveia, Rodrigo Barros, Suellyn Schopping

Trata-se de uma aplicação tipo FastAPI para listar produtos por um detemrinado ID e validar cupons de desconto.

Os produtos estão definidos em uma variável em src/api/main.py. Em um caso real seria necessário a conexão com banco de dados.

Foi inserida uma classe CupomDesconto para gerenciar e validar os cupons informados via api.

Para instalar o repositório:

1)  Clona o repositório
    git clone https://github.com/hen-ri-que/projeto_ibmec_01.git

2)  Instala o ambiente virtual
    python -m venv venv 

3) Ativa o ambiente virtual (windows)
   ./venv/Script/activate

4) Atualiza o pip
    python -m pip install pip --upgrade

5)  Instala as dependências de requirements.txt
    pip install -r requirements.txt

6) Rode a aplicação com uvicorn ou execute 
    uvicorn src.api.main:app --reload  
    
