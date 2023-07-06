import serial
import time
import requests

# Set up serial port
serial_port = "COM26"  # Update with your serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# ThingSpeak parameters
api_key = "FG63J0NGI9IO4G6F"  # Replace with your ThingSpeak API key
url = f"https://api.thingspeak.com/update.json"
count = 0

while True:
    line = ser.readline().decode("latin-1").strip()
    # print(line)
    if line.startswith("X:"):
        data = line.split(",")
        x = data[0].split(":")[1].strip()
        y = data[1].split(":")[1].strip()
        z = data[2].split(":")[1].strip()
        print(x, y, z)
        x = float(x)
        y = float(y)
        z = float(z)
        #     # print("hello")
        #     # x = int(x)
        #     # y = int(y)
        #     # z = int(z)
        count = count + 1
        if count == 100:
            payload = {"api_key": api_key, "field1": x, "field2": y, "field3": z}
            response = requests.get(url, params=payload)
            count = 0
    #     print(f"Response: {response.status_code} {response.text}")

# Close the serial port
ser.close()
