from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

root= Tk()
root.title("Weather Forecast")
root.geometry("800x800")
root['background']='white'



dt = datetime.datetime.now() 
date = Label(root, text=dt.strftime('%A -'), bg='white', font=("bold", 15)) 
date.place(x=5, y=130) 
month = Label(root, text=dt.strftime('%d %B %Y'), bg='white', font=("bold", 15)) 
month.place(x=100, y=130) 
  
# Time 
hour = Label(root, text=dt.strftime('%I : %M %p'), bg='white', font=("bold", 15)) 
hour.place(x=10, y=160) 

# City Search 
city_name = StringVar() 
city_entry = Entry(root, textvariable=city_name, width=70) 
city_entry.grid(row=1, column=0, ipady=8, padx=10, stick=W+E+N+S) 
  
def city_name(): 
    # API Call 
    api_key="f750d84c729f836d2b37db561f418eb8"
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city_entry.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    
    # Temperatures 
    y = api['main'] 
    current_temprature = y['temp'] 
    humidity = y['humidity'] 
    tempmin = y['temp_min'] 
    tempmax = y['temp_max'] 
  
    # Country 
    z = api['sys'] 
    country = z['country'] 
    city = api['name'] 
  
    # Adding the received info into the screen 
    lable_temp.configure(text=current_temprature) 
    lable_humidity.configure(text=humidity) 
    max_temp.configure(text=tempmax) 
    min_temp.configure(text=tempmin) 
    lable_country.configure(text=country) 
    lable_city.configure(text=city) 
  
  
# Search Bar and Button 
city_nameButton = Button(root, text="Search", command=city_name) 
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S) 
  
# Country  Names and Coordinates 
lable_city = Label(root, text="...", width=0,  
                   bg='white', font=("bold", 15)) 
lable_city.place(x=10, y=60) 
  
lable_country = Label(root, text="...", width=0,  
                      bg='white', font=("bold", 15)) 
lable_country.place(x=135, y=60) 

# Current Temperature 
lable_temp = Label(root, text="...", width=0, bg='white', 
                   font=("Helvetica", 100), fg='black') 
lable_temp.place(x=18, y=210) 
  
# Other temperature details 
humi = Label(root, text="Humidity: ", width=0,  
             bg='white', font=("bold", 15)) 
humi.place(x=3, y=380) 
  
lable_humidity = Label(root, text="...", width=0, 
                       bg='white', font=("bold", 15)) 
lable_humidity.place(x=107, y=380) 
  
  
maxi = Label(root, text="Max. Temp : ", width=0,  
             bg='white', font=("bold", 15)) 
maxi.place(x=3, y=410) 
  
max_temp = Label(root, text="...", width=0,  
                 bg='white', font=("bold", 15)) 
max_temp.place(x=128, y=410) 
  
mini = Label(root, text="Min. Temp : ", width=0,  
             bg='white', font=("bold", 15)) 
mini.place(x=3, y=440) 
  
min_temp = Label(root, text="...", width=0,  
                 bg='white', font=("bold", 15)) 
min_temp.place(x=128, y=440) 


root.mainloop()
