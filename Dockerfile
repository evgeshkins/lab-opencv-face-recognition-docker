FROM python:3.10-slim

RUN apt-get update && apt-get-install -y \
    libopencv-dev \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY face_recognition.py /app/
COPY data/input.jpg /app/

CMD ["python3", "face_recognition.py"]