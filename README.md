# Sistema de Gerenciamento de Ordens de Serviço (OS)

Solução Full Stack para gerenciamento de ordens de serviço, composta por uma API REST em Django e uma interface moderna em React/Vite.

## 🚀 Funcionalidades

- **Autenticação e Autorização**: Controle de acesso para técnicos e administradores.
- **Gestão de OS**: Criação, listagem e detalhamento de Ordens de Serviço.
- **Ações Técnicas**: Endpoint exclusivo para técnicos assumirem ordens abertas (`assumir`).
- **Controle de Status**: Fluxo de estados (Ex: `aberto` -> `em_andamento` -> `concluido`).

## 🛠️ Tecnologias

- **Backend**: Python 3.12, Django, Django REST Framework.
- **Frontend**: React (Vite).
- **Banco de Dados**: PostgreSQL.
- **Infraestrutura**: Docker & Docker Compose.

## 🗂️ Estrutura do Projeto

```text
    .
    ├── backend                 # API Django e Lógica de Negócio
    │   ├── core/               # Configurações do projeto
    │   ├── os_servico/         # App de Ordens de Serviço (Modelos, Views, Actions)
    │   ├── users/              # Gerenciamento de usuários e permissões
    │   └── manage.py
    ├── frontend                # Interface React / Vite
    │   ├── src/                # Componentes e Páginas
    │   └── vite.config.js
    ├── infra                   # Orquestração de containers
    │   └── docker-compose.yml
    └── README.md
```

## ⚙️ Configuração e Execução

    O projeto está totalmente dockerizado para facilitar o desenvolvimento.

1. **Clone o repositório:**
   ```bash
    git clone git@github.com:reginaldo-castro/iktos.git
    cd iktos
    ```
2. **Suba o ambiente completo (Backend, Frontend e DB):**
    ```bash
    cd infra
    docker-compose up --build
    ```
    
## 🔐 Autenticação e Acesso
    ```bash
        O sistema utiliza autenticação via Token. Conforme as regras de negócio:
        Token Expirado: Quando o token de acesso expira, 
        o sistema redireciona o usuário automaticamente para a tela de login.
    ```
    Criar Superusuário (Backend)

    docker-compose exec backend python manage.py createsuperuser

## 🗑️ Parar os containers
    ```
    docker-compose down
    ``