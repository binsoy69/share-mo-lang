from app import app
from qrcode import QRCode
from PIL import Image
import socket

def get_local_ip():
    try:
        # Gets the local IP used by the laptop (Wi-Fi or hotspot)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def show_qr_image(ip):
    url = f"http://{ip}:5000"
    qr = QRCode(border=2)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()  # ← This opens the QR image in default viewer
    print(f"\n🔗 Scan this QR or visit: {url}\n")

if __name__ == "__main__":
    ip = get_local_ip()
    show_qr_image(ip)
    app.run(host="0.0.0.0", port=5000)
