# 📬 Sistema de Contato - MUPI

Sistema web desenvolvido em Django para receber e gerenciar mensagens de contato. Inclui uma landing page pública para envio de mensagens e um painel administrativo protegido por autenticação para visualização das mensagens recebidas.

---

## 📋 Funcionalidades

- ✅ **Landing Page** (`/`) - Formulário de contato com validações
- ✅ **Validação de Email** - Verifica se o e-mail é válido
- ✅ **Validação de Nome** - Exige pelo menos dois nomes (nome e sobrenome)
- ✅ **Limite de Caracteres** - Mensagens limitadas a 1000 caracteres
- ✅ **Sistema de Login** (`/login/`) - Autenticação de usuários
- ✅ **Painel Administrativo** (`/painel/`) - Visualização das mensagens (acesso restrito)
- ✅ **Admin Django** (`/admin/`) - Painel administrativo do Django
- ✅ **Logout** (`/logout/`) - Encerramento seguro da sessão
- ✅ **Proteção CSRF** - Segurança contra ataques CSRF habilitada

---

## 🛠️ Tecnologias Utilizadas

- **Python** 3.x
- **Django** 4.2+
- **SQLite** (banco de dados padrão)
- **HTML/CSS** (templates)

---

## 🚀 Como Rodar a Aplicação

### Pré-requisitos

- Python 3.8 ou superior instalado
- Git (opcional, para clonar o repositório)

### Passo a Passo

#### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Eloany27Rodrigues/teste_mupi.git
cd teste_mupi
```

#### 2️⃣ Crie e ative um ambiente virtual

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5️⃣ Crie um superusuário (para acessar o painel)

```bash
python manage.py createsuperuser
```

Siga as instruções para definir usuário, email e senha.

#### 6️⃣ Execute o servidor

```bash
python manage.py runserver
```

#### 7️⃣ Acesse a aplicação

| Página | URL |
|--------|-----|
| 🏠 Landing Page | http://localhost:8000 |
| 🔐 Login | http://localhost:8000/login/ |
| 📊 Painel de Mensagens | http://localhost:8000/painel/ |
| ⚙️ Admin Django | http://localhost:8000/admin/ |
| 🚪 Logout | http://localhost:8000/logout/ |

> ⚠️ **Nota:** O painel de mensagens requer autenticação. Faça login primeiro!

---

## 📁 Estrutura do Projeto

```
teste_mupi/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── core/                   # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── contato/                # App principal
│   ├── models.py           # Modelo Mensagem
│   ├── views.py            # Views (landpage, painel)
│   ├── urls.py             # Rotas da aplicação
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       ├── landpage.html   # Página inicial com formulário
│       ├── login.html      # Página de login
│       └── painel.html     # Painel de mensagens
└── static/
    ├── css/
    └── images/
```

---

## 📝 Modelo de Dados

### Mensagem

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | CharField(100) | Nome completo do remetente |
| `email` | EmailField | E-mail do remetente |
| `mensagem` | TextField | Conteúdo da mensagem |
| `data_envio` | DateTimeField | Data/hora do envio (automático) |

---

## 🔒 Validações do Formulário

- **Nome:** Deve conter pelo menos dois nomes (ex: "João Silva")
- **Email:** Deve ser um e-mail válido
- **Mensagem:** Máximo de 1000 caracteres

---

## 🔐 Segurança

- ✅ View do painel protegida com `@login_required`
- ✅ Validação de email no backend
- ✅ Proteção CSRF habilitada
- ✅ Autenticação via sistema do Django

---
