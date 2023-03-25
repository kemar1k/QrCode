import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.utils import platform
from pyzbar.pyzbar import decode
from PIL import Image
from plyer import camera

class QRScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QRScanner, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Создаем таймер, который будет вызывать функцию сканирования QR каждую секунду
        Clock.schedule_interval(self.scan_qr, 1)

    def scan_qr(self, *args):
        # Получаем кадр с камеры и конвертируем его в изображение
        if platform == 'android':
            # Используем API для захвата изображения с камеры на Android
            image_data = camera.take_picture()
            image = Image.open(image_data)
        else:
            # Используем OpenCV для захвата изображения с камеры на других платформах
            import cv2
            capture = cv2.VideoCapture(0)
            capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            ret, frame = capture.read()
            capture.release()
            image = Image.fromarray(frame)

        # Декодируем QR-код
        decoded = decode(image)

        # Если QR-код найден, выводим его значение
        if len(decoded) > 0:
            print(decoded[0].data.decode())

class QRScannerApp(App):
    def build(self):
        return QRScanner()


if __name__ == '__main__':
    QRScannerApp().run()