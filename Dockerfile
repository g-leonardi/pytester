# Usa un'immagine Python ufficiale
FROM python:3.10-slim

# Imposta la working directory
WORKDIR /app

# Copia tutto il progetto dentro il container
COPY . .

# Installa requirements
RUN pip install --no-cache-dir -r requirements.txt

# Comando di default: esegui i test
CMD ["pytest", "-v"]