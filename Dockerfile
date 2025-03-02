# 使用 Python 3.10 基底映像
FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 複製專案檔案
COPY . .

# 安裝依賴套件
RUN pip install -r requirements.txt

# 啟動應用程式
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
