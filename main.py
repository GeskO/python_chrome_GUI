import eel
import pyowm

owm = pyowm.OWM("API KEY")
eel.init("web")


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    print(f"В городе {place} сейчас {str(temp)} градусов")
    return f"В городе {place} сейчас {str(temp)} градусов"


eel.start("main.html", size=(700, 380))
