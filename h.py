

import tkinter as tk
import time
import requests
root=tk.Tk()
root.title("Weather App")

def getWeather(root):
    city=textField.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    _data=requests.get(api).json()
    condition=_data['weather'][0]['main']
    temp=int(_data['main']['temp']-273.15)
    pressure=_data['main']['pressure']
    humidity=_data['main']['humidity']
    wind=_data['wind']['speed']
    sunrise=time.strftime()
    

    final_info="Sky:"+condition + "\n"+"Temparature:"+str(temp) +"c"+str(pressure)+str(humidity)+str(wind)
    label.config(text=final_info)
    
textField=tk.Entry(root,justify="center",width=20,font=("poppins",15,"bold"))
textField.pack(pady=20)
textField.focus()
textField.bind("<Return>",getWeather)
label=tk.Label(root,font=("poppins",15,"bold"))
label.pack()
root.mainloop()
