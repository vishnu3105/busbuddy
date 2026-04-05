# BusBuddy

Real-time crowd intelligence for Tamil Nadu's MTC bus network.

## The Problem

I rely on public transport daily as a student. Carrying a laptop,
navigating crowded MTC buses is a real struggle — and it's not
just me. Families with kids, elderly passengers, daily commuters —
everyone boards blind. You never know if the next bus is packed
until it's already in front of you.

That one minute of uncertainty costs time, comfort, and sometimes
the decision to take a different route entirely. I built BusBuddy
to fix that.

## What It Does

BusBuddy tells you the crowd status of an incoming bus before it
arrives at your stop. Board it, wait for the next one, or switch
to the train — your call. Now you actually have the data to decide.

## Features

- YOLOv8 powered real-time people counting
- Live bus GPS tracking on map
- Your location shown alongside the bus
- Board or wait suggestion based on crowd level
- Clean consumer interface — no raw camera feed exposed

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | YOLOv8 (Ultralytics) |
| Camera | IP Webcam (Mobile) |
| Backend | Python + Flask |
| Maps | Leaflet.js + OpenStreetMap |
| Frontend | HTML + CSS + JS |
| Tunneling | ngrok |

## How to Run
```bash
pip install ultralytics opencv-python flask
python app.py
```

- Open IP Webcam on phone → Start Server
- Open `/bus_tracker` on phone browser → transmits GPS
- Open `http://localhost:5000` on laptop

## Built By

Vishnu · Tamil Nadu, India · 2026
