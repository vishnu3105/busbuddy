from flask import Flask, render_template, jsonify
import cv2
from ultralytics import YOLO
import threading

app = Flask(__name__)
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture('http://hello:hello@192.168.1.8:8080/video')
person_count = 0

def detect_loop():
    global person_count
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        results = model(frame)
        count = 0
        for result in results:
            for box in result.boxes:
                if int(box.cls) == 0:
                    count += 1
        person_count = count

thread = threading.Thread(target=detect_loop, daemon=True)
thread.start()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/count')
def count():
    return jsonify({'count': person_count})

if __name__ == '__main__':
    app.run(debug=False)