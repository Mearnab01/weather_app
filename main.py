from datetime import datetime
from tkinter import *
from tkinter import ttk
import requests
import os

win=Tk()
win.title("Weather App")
win.config(bg="orange")
win.geometry("500x700")

name_label=Label(win,text="My Weather App",font=("ariel",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

def data_get():
    city = city_name.get()
    api_key = os.environ["weather_api"]
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    data = requests.get(url).json()

    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"] - 273.15))+"°C")
    per_label1.config(text=data["main"]["pressure"])
    
    sunrise_timestamp = data["sys"]["sunrise"]
    sunrise_time = datetime.fromtimestamp(sunrise_timestamp)
    sunrise_label1.config(text=sunrise_time.strftime("%H:%M:%S %p"))

    sunset_timestamp = data["sys"]["sunset"]
    sunset_time = datetime.fromtimestamp(sunset_timestamp)
    sunset_label1.config(text=sunset_time.strftime("%H:%M:%S %p"))
    



list_name=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Lakshadweep", "Puducherry"
]

city_name=StringVar()
com=ttk.Combobox(win,text="My Weather App",font=("ariel",15,"bold"),values=list_name,textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather Climate",font=("ariel",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("ariel",20))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label=Label(win,text="Weather Description",font=("ariel",17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1=Label(win,text="",font=("ariel",10,"bold"))
wd_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("ariel",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("ariel",20))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label=Label(win,text="Pressure",font=("ariel",20))
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text="",font=("ariel",20))
per_label1.place(x=250,y=470,height=50,width=210)

sunrise_label=Label(win,text="Sunrise",font=("ariel",20))
sunrise_label.place(x=25,y=540,height=50,width=210)
sunrise_label1=Label(win,text="",font=("ariel",20))
sunrise_label1.place(x=250,y=540,height=50,width=210)

sunset_label=Label(win,text="Sunset",font=("ariel",20))
sunset_label.place(x=25,y=610,height=50,width=210)
sunset_label1=Label(win,text="",font=("ariel",20))
sunset_label1.place(x=250,y=610,height=50,width=210)

done_button=Button(win,text="Done",font=("ariel",15,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)
win.mainloop()