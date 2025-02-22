# Resmi Python imajını kullan
FROM python:3.9

# Çalışma dizinini belirle
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uygulamayı başlat
CMD ["python", "app.py"]
