from twilio.rest import Client  # Import the Twilio client
from ultralytics import YOLO
import time 
import subprocess
import sys
import socket

# Twilio credentials
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'a5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+15xxxxxxxx'
recipient_phone_number = '+9184xxxxxxxx'

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
                    print("Highly corroded")
                    message_body = 'Immediate maintenance care is required. Corrosion is highly critical.'
                elif class_label == '1':
                    print("Low corrosion detected")
                    message_body = 'Corrosion detected, but it is low.'
                elif class_label == '2':
                    print("Medium corrosion detected")
                    message_body = 'Corrosion detected, it is of medium intensity.'

                # Send Twilio SMS notification
                message = client.messages.create(
                    from_=twilio_phone_number,
                    body=message_body,
                    to=recipient_phone_number
                )
                print("Twilio SMS sent. SID:", message.sid)
