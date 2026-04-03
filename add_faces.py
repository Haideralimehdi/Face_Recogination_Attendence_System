import cv2
import pickle
import numpy as np
import os
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data=[]
i=0
name=input("Enter your name: ")


while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_image = frame[y:y + h, x:x + w, : ]
        resize_img = cv2.resize(crop_image, (200, 200))
        if len(faces_data) < 100 and i % 10 == 0:
            faces_data.append(resize_img)
        i += 1
        cv2.putText(frame, f'Count: {len(faces_data)}' , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or len(faces_data) >= 100:
        break

video.release()
cv2.destroyAllWindows()


faces_data = np.array(faces_data)
faces_data = faces_data.reshape(100, -1) 


if "name.pkl" not in os.listdir("data/"):
    names = [name]*100
    with open("data/name.pkl", "wb") as f:
        pickle.dump(names, f)
else:
    with open("data/name.pkl", "rb") as f:
        names = pickle.load(f)
    names = names + [name]*100
    with open("data/name.pkl", "wb") as f:
        pickle.dump(names, f)

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)