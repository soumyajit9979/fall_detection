import serial
from twilio.rest import Client

# Twilio credentials
account_sid = "AC6b4eb901e1a001899b26646910090c57"
auth_token = "1a92ba8797729a92baf0a761580d1269"
twilio_number = "+14846421339"
recipient_number = "+917218984194"

# Serial communication settings
arduino_port = "COM26"  # Update with your Arduino port
baud_rate = 115200

# serial connection
ser = serial.Serial(arduino_port, baud_rate)

# Twilio client
client = Client(account_sid, auth_token)

while True:
    # Read data from the Arduino
    data = ser.readline().decode().strip()
    print(data)  # Optional: Print received data for debugging

    # Check if data equals "patient fell"
    if data == "patient fell":
        # Send the message via Twilio
        message = client.messages.create(
            body="Patient has fallen!", from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")

# Close the serial connection
ser.close()
