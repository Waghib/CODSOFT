import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from ttkthemes import ThemedTk
from datetime import datetime

class WeatherApp(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("breeze")
        self.title("Weather App")
        self.geometry("400x420")

        self.style = ttk.Style(self)

        self.big_frame = ttk.Frame(self)
        self.big_frame.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):

        # Header Frame
        header_frame = tk.Frame(self.big_frame, bg='#3DAEE9')
        header_frame.pack(fill="x")

        # Header Label
        header_label = ttk.Label(header_frame, text="Weather App", font=('Helvetica', 16), foreground='white', background='#3DAEE9')
        header_label.pack(pady=10)

        self.upperFrame = ttk.Frame(self.big_frame)
        self.upperFrame.pack(pady=5)

        # City input
        self.city_label = ttk.Label(self.upperFrame, text="Enter City:", font=('Helvetica', 14))
        self.city_label.grid(row=0, column=0, pady=10)
        
        self.city_entry = ttk.Entry(self.upperFrame)
        self.city_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to get weather
        self.get_weather_button = ttk.Button(self.big_frame, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.bottomFrame = ttk.Frame(self.big_frame, style='My.TFrame')
        self.bottomFrame.pack(pady=5, fill="both")
        self.style.configure('My.TFrame', background='#272625')

        # Display weather labels
        self.weather_description_label = ttk.Label(self.bottomFrame, text="Weather: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.weather_description_label.grid(row=0, column=0, padx=20, pady=11, sticky=tk.W)

        self.temperature_label = ttk.Label(self.bottomFrame, text="Temperature: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.temperature_label.grid(row=1, column=0, padx=20, pady=11, sticky=tk.W)

        self.feel_like_label = ttk.Label(self.bottomFrame, text="Feels Like: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.feel_like_label.grid(row=2, column=0, padx=20, pady=11, sticky=tk.W)

        self.humidity_label = ttk.Label(self.bottomFrame, text="Humidity: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.humidity_label.grid(row=3, column=0, padx=20, pady=11, sticky=tk.W)

        self.wind_speed_label = ttk.Label(self.bottomFrame, text="Wind Speed: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.wind_speed_label.grid(row=4, column=0, padx=20, pady=11, sticky=tk.W)

        self.time_label = ttk.Label(self.bottomFrame, text="Time: ", font=('Helvetica', 12), foreground='white', background='#272625')
        self.time_label.grid(row=5, column=0, padx=20, pady=11, sticky=tk.W)

    def get_weather(self):
        city = self.city_entry.get()

        if not city:
            messagebox.showwarning("Input Error", "Please enter a city.")
            return

        # API key here
        api_key = "99981ed39b5361e23b7ba728dae492ca"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"

        url = base_url + "q=" + city + "&appid=" + api_key

        try:
            response = requests.get(url)
            data = response.json()
            # print(data) # to check the data in JSON

            if response.status_code == 200:

                weather_description = data['weather'][0]['description']
                temp_kelvin = data['main']['temp']
                feels_like_kelvin = data['main']['feels_like']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                time = data['dt']

                temp_celsius, temp_fahrenheit = self.temeratureConversion(temp_kelvin)
                feels_like_celsius, feels_like_fahrenheit = self.temeratureConversion(feels_like_kelvin)

                # Update labels with weather information
                self.weather_description_label.config(text=f"Weather: {weather_description}")
                self.temperature_label.config(text=f"Temperature: {round(temp_celsius)}°C or {temp_fahrenheit:.2f}°F")
                self.feel_like_label.config(text=f"Feels Like: {round(feels_like_celsius)}°C or {round(feels_like_fahrenheit)}°F")
                self.humidity_label.config(text=f"Humidity: {humidity}%")
                self.wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
                self.time_label.config(text=f"Time: {self.format_time(time)}")

            else:
                messagebox.showerror("Error", f"Failed to get weather data. Error code: {response.status_code}")
                
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def temeratureConversion(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit
    
    def format_time(self, time):
        # Convert Unix timestamp to datetime object
        dt_object = datetime.utcfromtimestamp(time)
        # Format datetime object as a string
        formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time

# temp, feel like, description, humidity, wind speed, time

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
