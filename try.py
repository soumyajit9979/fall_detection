import serial
import requests
from twilio.rest import Client

# Twilio credentials
account_sid = "AC6b4eb901e1a001899b26646910090c57"
auth_token = "1a92ba8797729a92baf0a761580d1269"
twilio_number = "+14846421339"
recipient_number = "+919429756022"

# ThingSpeak credentials
api_key = "FG63J0NGI9IO4G6F"
channel_url = "https://api.thingspeak.com/update"

# Serial communication settings
arduino_port = "COM26"  # Update with your Arduino port
baud_rate = 115200

# Initialize the serial connection
ser = serial.Serial(arduino_port, baud_rate)

# Initialize the Twilio client
client = Client(account_sid, auth_token)

while True:
    # Read data from the Arduino
    data = ser.readline().decode().strip()
    print(data)  # Optional: Print received data for debugging

    # Send data to ThingSpeak
    # payload = {"api_key": api_key, "field1": data}
    # response = requests.get(channel_url, params=payload)
    # if response.status_code == 200:
    #     print("Data sent to ThingSpeak successfully!")
    # else:
    #     print("Failed to send data to ThingSpeak!")

    # Check if data equals "patient fell"
    if data == "patient fell":
        # Send the message via Twilio
        message = client.messages.create(
            body="Patient has fallen!", from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")


# Close the serial connection
ser.close()
