# Usa uma imagem oficial do Python
FROM python:3.9-slim

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
