from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7ef6c3db4f0dc5069bf6e614ad522759").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    per_label1.config(text=data["main"]["pressure"])
    temp = int(data["main"]["temp"]-273.15)
    temp_label1.config(text=temp)
    personalized_msg = get_personalized_msg(temp)
    msg_label.config(text=personalized_msg)

def get_personalized_msg(temp):
    if temp < 10:
        return "It's very cold!"
    elif temp < 20:
        return "It's a bit chilly."
    elif temp < 30:
        return "Enjoy the pleasant weather."
    else:
        return "It's quite hot outside!"

win = Tk()
win.title("My Weather App")
win.geometry("500x600")

# Set the background image
bg = PhotoImage(file="C:\\Users\\Anup\\Documents\\cloudsky1.png")
bg_label = Label(win, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Other widgets
name_label = Label(win, text="Weather App",fg="skyblue", bg="black",anchor="center",font=("Trebuchet MS",25, "bold"))
name_label.place(x=120, y=50, height=50, width=250)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, text="Weather App", values=list_name, font=("Comic Sans MS", 20, "bold"), textvariable=city_name)

com.place(x=25, y=120, height=50, width=450)


w_label = Label(win, text="Weather Climate",fg="white",bg="black", font=("Georgia", 17,"italic"))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Georgia", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wd_label = Label(win, text="Weather Description", fg="white",bg="black",font=("Georgia", 16,"italic"))
wd_label.place(x=25, y=330, height=50, width=210)

wd_label1 = Label(win, text="", font=("Georgia", 17))
wd_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature",fg="white",bg="black", font=("Georgia", 17,"italic"))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="",font=("Georgia", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure",fg="white",bg="black", font=("Georgia", 17,"italic"))
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Georgia", 17))
per_label1.place(x=250, y=470, height=50, width=210)

msg_label = Label(win, text="", fg="white",bg="grey",font=("Georgia",16, "italic"))
msg_label.place(x=25, y=540, height=30, width=450)

done_button = Button(win, text="Done", fg="grey",bg="black", font=("Courier New", 20, "bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
