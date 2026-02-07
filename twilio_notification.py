from twilio.rest import Client  # Import the Twilio client
from ultralytics import YOLO
import time 
import subprocess
import sys
import socket

# Twilio credentials
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'a59xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+15xxxxxxxx'
recipient_phone_number = '+91xxxxxxxxxx'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Define the path to your custom weights file
custom_weights_file = 'best.pt'

# Initialize the YOLO model with custom weights
model = YOLO(custom_weights_file) 

# Define frame skip factor
frame_skip_factor = 6  # Adjust this value based on your requirements

# Define confidence thresholds for each class
confidence_thresholds = {'0': 0.5, '1': 0.75, '2': 0.7}
frame_count = 0
while cap.isOpened():
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1

    # Skip frames based on frame_skip_factor
    if frame_count % frame_skip_factor != 0:
        continue
    
    # Perform object detection on the frame
    results = model(frame)
    annotated = results[0].plot()
    # Iterate over the results for each image
    for detection in results:
        class_labels = detection.boxes.cls
        confidences = detection.boxes.conf

        # Check if any class confidence exceeds the threshold
        for class_label, confidence in zip(class_labels, confidences):
            class_label = str(int(class_label))  # Convert class label to string
            if class_label in confidence_thresholds and confidence > confidence_thresholds[class_label]:
                if class_label == '0':
                    print("highly corroded")
                    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    auth_token = 'a59xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    client = Client(account_sid, auth_token)
                    
                    message = client.messages.create(
                    from_='+15xxxxxxxx',
                    body='immediate maintenance care is required',
                    to='+9184xxxxxxxx'
                    )
                    print(message.sid)
                    
                elif class_label == '1':
                    print("Low")
                    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    auth_token = 'a59xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                    from_='+15xxxxxxxxx',
                    body='corrosion is low',
                    to='+9184xxxxxxxx'
                    )
                    print(message.sid)
                    
                    
                elif class_label == '2':
                    print("Medium")
                    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    auth_token = 'a59xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    client = Client(account_sid, auth_token)

                    message = client.messages.create(
                    from_='+15xxxxxxxx',
                    body='Mediumly corroded',
                    to='+9184xxxxxxxx'
                    )
                    print(message.sid)
                    
