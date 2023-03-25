import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from pyzbar.pyzbar import decode
from PIL import Image
import cv2


class QRScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QRScanner, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Создаем камеру
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Создаем таймер, который будет вызывать функцию сканирования QR каждую секунду
        Clock.schedule_interval(self.scan_qr, 1)

    def scan_qr(self, *args):
        # Получаем кадр с камеры и конвертируем его в изображение
        ret, frame = self.capture.read()
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

# import kivy
# from kivy.uix.label import Label
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.core.window import Window

# Window.size = (375,812)
# Window.title = 'Diplom_App'

# class QRscannWidget(BoxLayout):
#     def clicker_func(self, instance):
#         print(instance.text + 'was clicked')
    

# class QRscannApp(App):
#     def build(self):
#         return QRscannWidget()

# if __name__ == '__main__':
#     QRscannApp().run()