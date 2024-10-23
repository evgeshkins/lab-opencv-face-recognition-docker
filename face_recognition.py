import cv2
import sys

image_path = 'data/input.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not load image from {image_path}")
    sys.exit()

# Конвертируем изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Загружаем предобученный каскад для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Обнаружение лиц
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

# Вывод результатов
if len(faces) == 0:
    print("No faces detected.")
else:
    print(f"Detected {len(faces)} faces.")
    for (x, y, w, h) in faces:
        print(f"Face at X: {x}, Y: {y}, Width: {w}, Height: {h}")
