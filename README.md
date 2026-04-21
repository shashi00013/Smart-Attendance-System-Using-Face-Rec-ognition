# 📸 Smart Attendance System Using Face Recognition

> AI-powered attendance management with real‑time face detection and automatic logging.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org)
[![FaceRecognition](https://img.shields.io/badge/face_recognition-1.3+-informational)](https://github.com/ageitgey/face_recognition)
[![License](https://img.shields.io/badge/License-Educational%20Use%20Only-blue)](LICENSE)

---

## 📌 Project Overview

This system eliminates proxy attendance and manual errors by using **facial recognition** to mark student attendance automatically.  
It captures a student’s face via webcam, matches it against stored encodings, and logs the attendance with date and time.

### Key Features

- ✅ **Real‑time face detection** using OpenCV & `face_recognition`
- ✅ **Automatic attendance marking** – press `s` when your face is detected
- ✅ **Admin dashboard** to manage students, view attendance, and export reports
- ✅ **Face encoding storage** – each student’s unique face signature is saved in SQLite
- ✅ **Prevents proxy attendance** – only the registered person can mark attendance
- ✅ **Export reports** to **Excel** (XLSX) and **PDF** formats
- ✅ **Two ways to add students** – upload an image or capture directly from webcam

---

## 🛠️ Tech Stack

| Component          | Technology                                |
|--------------------|--------------------------------------------|
| Backend            | Flask (Python)                             |
| Face Recognition   | `face_recognition` (dlib‑based), OpenCV    |
| Database           | SQLite                                     |
| Frontend           | HTML, CSS, Jinja2 templates                |
| Report Generation  | Pandas (Excel), pdfkit (PDF)               |

---

## 📸 Screenshots (Preview)
<img width="1536" height="1024" alt="81bbd4d8-6aab-4a4a-90dc-8561293fdfd8" src="https://github.com/user-attachments/assets/6f4178ef-f28f-4f8e-a874-1c30e62edf73" />



## ⚙️ Installation & Setup

### Prerequisites

- Python 3.9 or higher
- Webcam (built‑in or external)
- Git

### Step‑by‑step

1. **Clone the repository**
   ```bash
   git clone https://github.com/shashi00013/Smart-Attendance-System-Using-Face-Recognition.git
   cd Smart-Attendance-System-Using-Face-Recognition
Create a virtual environment

bash
python -m venv venv
Activate it

Windows:

bash
venv\Scripts\activate
Linux / macOS:

bash
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Note for Windows users: dlib can be tricky. Install a pre‑compiled wheel:

bash
pip install dlib‑19.24.2‑cp39‑cp39‑win_amd64.whl
Or use pip install face-recognition which will attempt to build it.

Run the application

bash
python app.py
Open your browser at http://127.0.0.1:5000

📁 Project Structure
text
smart_attendance/
│
├── app.py                 # Main Flask application
├── face_utils.py          # Face encoding & recognition logic
├── database.py            # SQLite helper functions
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── admin_dashboard.html
│   ├── add_student.html
│   ├── take_attendance.html
│   └── view_reports.html
├── uploads/               # Temporary student images (auto‑created)
└── attendance_records/    # Exported Excel/PDF reports (auto‑created)
🧠 How It Works (Flow)
Admin adds a student – either by uploading a clear face image or using the webcam to capture one.

Face encoding is generated using face_recognition and stored as a blob in SQLite.

During attendance – the system starts the webcam, detects faces in real time.

When a face is recognised, the student ID is displayed.

Admin presses s to mark attendance for that student with today’s date.

Attendance is stored in the database (only one entry per student per day).

Reports can be exported as Excel or PDF from the admin panel.

👨‍💻 Developer
Shashi Kumar
B.Tech Computer Science Engineering (2023–2027)
CGC University, Mohali

GitHub: shashi00013

Email: sk5251476@gmail.com

LinkedIn: linkedin.com/in/shashi0013

🚀 Motivation
Manual attendance is time‑consuming and prone to proxy marking. As classes grew larger, I saw the need for an automated, contactless, and secure solution.
This project uses state‑of‑the‑art face recognition to ensure that only the genuine student can mark their presence – improving accuracy and saving valuable lecture time.

🔮 Future Enhancements
📊 Live dashboard showing today’s attendance percentage

📧 Email alerts to absent students or parents

📱 Mobile app (React Native) with QR code fallback

☁️ Cloud deployment (AWS/Heroku) for multiple classrooms

🎤 Voice assistant integration for hands‑free operation

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a feature branch (git checkout -b feature/NewFeature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/NewFeature)

Open a Pull Request

Please follow PEP8 and write meaningful commit messages.

📄 License
This project is for educational use only. Not intended for commercial purposes.
You may use, modify, and share it for learning and internal college projects.

🙏 Acknowledgements
face_recognition – the easiest face recognition library

OpenCV – real‑time computer vision

Flask – lightweight web framework

SQLite – embedded database

⭐ If this project helped you, please give it a star on GitHub!
   
