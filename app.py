from flask import Flask, render_template, jsonify, request
import cv2
from ultralytics import YOLO
import threading

app = Flask(__name__)
model = YOLO('yolov8n.pt')
cap = cv2.VideoCapture('http://hello:hello@192.168.1.4:8080/video')
person_count = 0
bus_lat = 12.9249
bus_lng = 80.1000

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

@app.route('/update_location', methods=['POST'])
def update_location():
    global bus_lat, bus_lng
    data = request.get_json()
    bus_lat = data['lat']
    bus_lng = data['lng']
    return jsonify({'status': 'ok'})

@app.route('/bus_location')
def bus_location():
    return jsonify({'lat': bus_lat, 'lng': bus_lng})

@app.route('/bus_tracker')
def bus_tracker():
    return render_template('bus_tracker.html')

if __name__ == '__main__':
    app.run(debug=False)