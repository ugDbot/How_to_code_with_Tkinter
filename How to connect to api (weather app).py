from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
import requests
import json

app = Tk()
app.title("Weather app")
app.iconbitmap("C:/Users/admin/Pictures/company.ico")
app.geometry("600x100")





#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89004&distance=25&API_KEY=5EA0D75A-6741-4932-BFF9-F86B8358D969





#create zip code look up function
def ziplookup():
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=5EA0D75A-6741-4932-BFF9-F86B8358D969")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "light green"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "yellow"
        elif category == "Unhealthy":
            weather_color = "red"
        elif category == "Very Unhealthy":
            weather_color = "dark red"
        elif category == "Hazardous":
            weather_color = "purple"

        app.configure(background=weather_color)

        lbl = Label(app, text=city + " " + "Air Quality" + " " + str(quality) + " " + category,
                    font=("Helvetica", 20), background=weather_color)
        lbl.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error...."


zip = Entry(app)
zip.grid(row=0, column=1, stick=W+E+N+S)

zip_btn = Button(app, text="Look up Zip Code", command= ziplookup)
zip_btn.grid(row=0, column=0, stick=W+E+N+S)

app.mainloop()