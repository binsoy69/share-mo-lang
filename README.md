# 📁 share-mo-lang: Flask-Based File Transfer Web App

A minimal, browser-accessible file transfer app inspired by ShareIt — designed for use over local Wi-Fi or a hotspot without internet. Share files between a laptop (server) and Android device through a secure, password-protected web interface.

---

## 🚀 Features

- 🔁 **Two-way file transfer** (Laptop ↔ Android)
- 🌐 **Offline support** — works over hotspot or LAN without internet
- 📂 File upload/download via browser
- 🔒 **PIN/password-protected** access
- 📱 **QR code popup** for fast phone access
- 🧼 Clean, mobile-friendly UI
- 🗑️ Delete buttons for uploaded files
- 📦 Packaged as a standalone `.exe` (Windows) — no Python required

---

## 🛠 Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JS
- **Packaging**: PyInstaller (.exe build for Windows)
- **Libraries**: Flask, qrcode, Pillow

---

## 🧾 Options to Run

### 🖥️ Option 1: For End Users (No Python Required)

If you're using the **`.exe` file** version:

1. Navigate to `dist/` folder
2. Double-click `run.exe`
3. A QR code will appear — scan it or enter the IP shown in your phone's browser
4. Enter the password and start sharing files!

> 🔒 Make sure `uploads/` folder is in the same directory as `run.exe`

---

### 👨‍💻 Option 2: For Developers (Python Installed)

1. **Clone the repo**
   ```bash
   git clone https://github.com/binsoy69/share-mo-lang.git
   ```
2. **Create and activate a virtual environment**
    ```bash
    conda create -n shareit python=3.10
    conda activate shareit
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Create .env file**
    ```bash
    FLASK_SECRET_KEY=your_secret_key_here
    FILE_TRANSFER_PASSWORD=your_password_here
    ```
5. **Run the app**
    ```bash
    python run.py
    ```
### 🧩 File Layout
```
share-mo-lang/
├── dist
      └── run.exe        ← for Windows users
├── run.py               ← main launcher (QR + app)
├── app.py
├── .env
├── templates/
      └── index.html
      └── upload.html
├── static/
      └── style.css
      └── script.js
├── uploads/
├── requirements.txt
└── README.md
```
### 📲 How It Works
- App launches and detects your laptop's IP
- Generates and displays a QR code image
- Android device connects to http://<your-ip>:5000
- User logs in using PIN/password
- Files are stored in uploads/ directory




