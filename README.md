# Daana App

A web application for Sri Lankan Buddhist temples to manage Daana (almsgiving) bookings.

## About

This platform allows temples to register, list available monks/helpers, and manage bookings, while donors browse availability and reserve dates.

## Setup

1. Copy `.env.example` to `.env` and configure:
   ```
   HOST=0.0.0.0
   PORT=8001
   DEBUG=False
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   python server.py
   ```

The app will be available at `http://localhost:3000`

## Development

- Edit `server.py` to add API endpoints
- Update `index.html` for the landing page
- Add more static files as needed

## Deployment

This app uses GitHub Actions for automated deployment via SSH to your server.

Configure the following GitHub Secrets:
- `SSH_HOST`: Your server address (e.g., `your-server-ip -p 22`)
- `SSH_USERNAME`: Your server username
- `DEPLOY_SSH_KEY`: Private SSH key with read+write access to the repo
- `DEPLOY_PATH`: `/var/www/daana` (where the app will be deployed)

Push to `main` branch to trigger deployment.

## Features

- Simple HTTP server using Python's built-in http.server
- CORS support for frontend applications
- Static file serving
- Easy to extend with Flask/Django later
