# Usa uma imagem oficial do Python
FROM python:3.9-slim@sha256:9aa5793609640ecea2f06451a0d6f379330880b413f954933289cf3b27a78567

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o app usa
EXPOSE 5000

# Comando padrão para rodar a aplicação
CMD ["python", "app.py"]
