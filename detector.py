import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture('http://hello:hello@192.168.1.4:8080/video')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    
    person_count = 0
    for result in results:
        for box in result.boxes:
            if int(box.cls) == 0:  # 0 = person in YOLO
                person_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(frame, f'People: {person_count}', (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    
    cv2.imshow('Bus Crowd Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
