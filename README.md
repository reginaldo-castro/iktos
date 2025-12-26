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
       docker compose -f infra/docker-compose.yml up --build
    ```

## 🔐 Autenticação e Acesso
```bash
    O sistema utiliza autenticação via Token.
    Token Expirado: Quando o token de acesso expira, 
    o sistema redireciona o usuário automaticamente para a tela de login.
```

## Criar Superusuário (Backend)
```bash
    docker exec -it os_backend(nome_do_container) python manage.py createsuperuser
    nome_do_container pode usar o docker ps para visualizar o nome
```

## 🛠️ Administração e Acesso Direto

Esta seção é destinada a administradores para a gestão de dados mestres do sistema.

* **Painel Administrativo**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
    * Utilizado para gerenciar **Checklists** e configurações globais.
    * **Cadastrar usuários**: Criação e gestão de técnicos e permissões.

### Fluxo de Cadastro
Para o funcionamento correto do sistema, o administrador deve:
1.  **Cadastrar Técnicos**: Criar os usuários que utilizarão o sistema.
2.  **Configurar Checklists**: Definir os itens de verificação para as OS.
3.  **Cadastrar Ordens de Serviço**: Iniciar o fluxo de trabalho para os técnicos.

## 🗑️ Parar os containers
```
    docker compose -f infra/docker-compose.yml down
```

---

## 👤 Autor

Desenvolvido por **Reginaldo Castro**.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/reginaldo-castro)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/reginaldo-rc-castro/)

---

> Este é um prototipo inicial usando as soluções Full Stack. Sinta-se à vontade para entrar em contato!