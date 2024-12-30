# 🚀 Sistema de Automação de RH - SNEAT Starter Kit

Este projeto implementa um sistema de **automação de processos de RH** utilizando o **SNEAT Starter Kit**.  
Desenvolvido em **Python/Django**, ele oferece funcionalidades para gestão e controle de processos administrativos.  

---

## 📋 **Funcionalidades**

- 📄 **Gerenciamento de Dados**: Processamento e validação de dados via interface web.  
- 📨 **Envio de Solicitações SOAP**: Comunicação com serviços externos para automação de tarefas.  
- 📊 **Exportação de Resultados**: Geração de arquivos processados no formato Excel.  
- 🛠️ **Configuração com Docker**: Suporte para ambientes conteinerizados usando Docker.  
- 🌐 **Integração Frontend-Backend**: Interfaces dinâmicas com templates personalizados.  

---

## 🛠️ **Pré-requisitos**

- **Python 3.10 ou superior**  
- **Pip** para gerenciamento de pacotes.  
- **Docker** e **Docker Compose** (opcional para implantação).  
- Banco de Dados SQLite (padrão) ou configurável no ambiente.  

---

## 🧩 **Instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/automacao-rh.git
   cd automacao-rh
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux/Mac
   .venv\Scripts\activate        # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo **`.env`**:
   ```plaintext
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   SECRET_KEY=super_secret_key
   SOAP_URL=https://isscuritiba.curitiba.pr.gov.br/Iss.NfseWebService/nfsews.asmx
   ```

---

## ⚙️ **Execução do Sistema**

1. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver


2. Usando Docker (Opcional):
   ```bash
   docker-compose up --build
   ```

---

## 📊 **Logs**

Logs são gerados automaticamente no arquivo **`soap_debug.log`** durante a execução. Certifique-se de revisar este arquivo para diagnosticar erros.

---

## 🧑‍💻 **Tecnologias Utilizadas**

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS (via templates do Starter Kit)  
- **Banco de Dados:** SQLite (padrão)  
- **SOAP Requests:** Biblioteca Requests  
- **Ambiente:** Docker, Docker Compose  

---

## ❓ **Dúvidas ou Problemas?**

Caso encontre problemas ou tenha dúvidas, abra uma **issue** neste repositório ou entre em contato diretamente.

---

## 📝 **Licença**

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.
```
