FROM python:3.11-slim

# Install Java (required for language-tool-python)
RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY validator ./validator
COPY sample ./sample
COPY reports ./reports

CMD ["python", "-m", "validator.main"]
