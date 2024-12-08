Backend Sistema de Gestão do Cacau
Sistema desenvolvido em Django REST Framework para gerenciamento da produção e comercialização de cacau.
📋 Funcionalidades

Autenticação de usuários por email/senha com JWT
Cadastro e gestão de produtores
Controle de propriedades e endereços
Gestão de produção e lotes
Sistema de comercialização
Fermentação e processamento
Cadastro de empresas com upload de imagens
Sistema de filtragem por tipo de empresa

🔧 **Tecnologias Utilizadas**

Python 3.x
Django 5.1.1
Django REST Framework
JWT (JSON Web Token)
SQLite3
Pillow para manipulação de imagens
Django Filter para filtragem de dados

⚙️ **Instalação e Configuração**

1-Clone o repositório:
 ```bash
  git clone https://github.com/Connect-Cacau/Backend/
  cd Backend
 ```
2-Crie e ative o ambiente virtual:
 ```bash
  # Windows
  python -m venv venv
  venv\Scripts\activate
  
  # Linux/macOS
  python3 -m venv venv
  source venv/bin/activate
 ```
3-Instale as dependências:
 ```bash
  pip install -r requirements.txt
 ```
4.Execute as migrações:
 ```bash
  python manage.py makemigrations
  python manage.py migrate
 ```
5.Crie um superusuário:
 ```bash
  python manage.py createsuperuser
 ```
6.Inicie o servidor:
 ```bash
  python manage.py runserver
 ```
**Endpoints da API**
**Autenticação**

POST /api/cadastro/ - Registro de usuário
POST /api/login/ - Login de usuário

**Gestão de Cacau**

GET/POST /api/cacau/ - Listar/Criar registros de cacau

GET/PUT/DELETE /api/cacau/{id}/ - Detalhar/Atualizar/Deletar registro específico

**Endereços**

GET/POST /api/endereco/ - Listar/Criar endereços

GET/PUT/DELETE /api/endereco/{id}/ - Detalhar/Atualizar/Deletar endereço

**Cadastros**

GET/POST /api/cadastro/ - Listar/Criar cadastros

GET/PUT/DELETE /api/cadastro/{id}/ - Detalhar/Atualizar/Deletar cadastro

**Produtores**

GET/POST /api/produtor/ - Listar/Criar produtores

GET/PUT/DELETE /api/produtor/{id}/ - Detalhar/Atualizar/Deletar produtor

**Comercialização**

GET/POST /api/comercializacao/ - Listar/Criar comercializações

GET/PUT/DELETE /api/comercializacao/{id}/ - Detalhar/Atualizar/Deletar comercialização

**Propriedades**

GET/POST /api/propriedade/ - Listar/Criar propriedades

GET/PUT/DELETE /api/propriedade/{id}/ - Detalhar/Atualizar/Deletar propriedade

**Produção**

GET/POST /api/producao/ - Listar/Criar produções

GET/PUT/DELETE /api/producao/{id}/ - Detalhar/Atualizar/Deletar produção

**Lotes**

GET/POST /api/lote/ - Listar/Criar lotes

GET/PUT/DELETE /api/lote/{id}/ - Detalhar/Atualizar/Deletar lote

**Fermentação**

GET/POST /api/fermentacao/ - Listar/Criar fermentações

GET/PUT/DELETE /api/fermentacao/{id}/ - Detalhar/Atualizar/Deletar fermentação

**Empresas**

GET/POST /api/empresas/ - Listar/Criar empresas

GET/PUT/DELETE /api/empresas/{id}/ - Detalhar/Atualizar/Deletar empresa

GET /api/empresas/?tipo=TIPO - Filtrar empresas por tipo

📝 **Exemplos de Requisições**

Registro de Usuário
```json
POST /api/cadastro/
{
    "user": {
        "email": "exemplo@email.com",
        "password": "senha123"
    },
    "nome": "Nome do Usuário",
    "estadoCivil": "Solteiro"
}
```

Login
```json
POST /api/login/
{
    "email": "exemplo@email.com",
    "password": "senha123"
}
```

Cadastro de Empresa
```json
POST /api/empresas/
{
    "nome": "Empresa de Chocolate",
    "tipo": "CHOCOLATE",
    "image": [arquivo binário]
}
```

Filtrar Empresas
GET /api/empresas/?tipo=CHOCOLATE

📦 Estrutura do Projeto
```json
backend/
├── cacau/                  # App principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── models.py          # Modelos do banco de dados
│   ├── serializers.py     # Serializers da API
│   ├── views.py           # Views da API
│   └── urls.py            # URLs da API
├── cacauDjango/           # Configurações do projeto
│   ├── settings.py        # Configurações gerais
│   ├── urls.py           # URLs principais
│   └── wsgi.py           # Configuração WSGI
├── requirements.txt       # Dependências do projeto
├── manage.py             # Script de gerenciamento
└── README.md             # Este arquivo
```




