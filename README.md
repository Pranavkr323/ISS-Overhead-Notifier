# ISS Overhead Notifier 🚀

A Python automation project that tracks the International Space Station (ISS) in real time and sends an email notification when the ISS is passing near the user's location during nighttime.

## Features
- Tracks the live position of the ISS.
- Checks whether the ISS is near the user's location.
- Determines if it is currently dark.
- Sends an automated email notification.
- Runs continuously and checks every 60 seconds.

## Technologies Used
- Python
- Requests
- Datetime
- SMTP

## APIs Used
- Open Notify API
- Sunrise-Sunset API

## How It Works
1. Fetches the current ISS coordinates.
2. Compares them with the user's location.
3. Checks whether it is nighttime.
4. Sends an email alert when both conditions are met.
