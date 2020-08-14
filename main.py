import eel
import pyowm

owm = pyowm.OWM("d86406cbd3667560013f12d40e475f56")
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
