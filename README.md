# Face Recognition Attendance System

A real-time **Face Recognition Attendance System** built with **Python, OpenCV, KNeighborsClassifier, Streamlit**, and **MySQL**. This project allows you to add new faces, recognize them in real-time, and automatically record attendance in a **MySQL database**. Attendance data can also be visualized via a **Streamlit dashboard**.

---

## Features

- 🖼 **Add New Faces**: Capture face data with your webcam and save it for recognition.
- 🎯 **Real-Time Recognition**: Detect and recognize faces using **OpenCV** and **K-Nearest Neighbors**.
- 💾 **Database Storage**: Attendance records and user info stored in **MySQL** for persistence.
- 📊 **Streamlit Dashboard**: View attendance in real-time with an interactive Streamlit web app.
- 🔊 **Voice Feedback**: Optional voice notification when attendance is taken.
- 📝 **CSV Export**: Optional export of attendance for backup or reporting.

---

## Project Structure
Face-Recognition-Attendance/

├── data/         # Haarcascade XML and face embeddings                                                   
│   ├── haarcascade_frontalface_default.xml                           
│   ├── faces_data.pkl                                                       
│   └── name.pkl                                                                      
│
├── Attendance/                 # CSV files for attendance records                                                 
│   └── Attendance_<date>.csv                                                           
│
├── add_face.py                 # Script to capture new faces and store in database                                         
├── test.py                     # Real-time recognition & attendance logging                                        
├── streamlit_app.py            # Streamlit dashboard for attendance visualization                              
├── requirements.txt            # Python dependencies                                          
└── background1.png             # UI background image for recognition

**Dependencies**
-Python 3.8+                        
-OpenCV (opencv-python)                                    
-NumPy                                                      
-scikit-learn                                            
-Streamlit                                                  
-streamlit-autorefresh                                          
-pywin32 (for Windows voice notifications)                                           
-pandas                                               
-mysql-connector-python                                                    
