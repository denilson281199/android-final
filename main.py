import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

URL_NGROK = "https://bleriest-portraitlike-dreama.ngrok-free.dev"

class SystemUpdateApp(App):
    def build(self):
        # Label simples atu hatene app funsiona
        return Label(text='System Update App\nRunning...')

    def on_start(self):
        # Chama funsaun kada 5 segundos
        Clock.schedule_interval(self.send_request, 5)

    def send_request(self, dt):
        try:
            response = requests.get(f"{URL_NGROK}/ping", timeout=5)
            print(f"Response: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    SystemUpdateApp().run()
