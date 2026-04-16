# Hello World App

A simple Hello World web application for the Daana platform.

## Setup

1. Copy `.env.example` to `.env` and configure:
   ```
   HOST=0.0.0.0
   PORT=3000
   DEBUG=False
   ```

2. Start the server:
   ```
   python server.py
   ```

## Deployment

This app uses the same deployment infrastructure as the TodoApp.

## Features

- Simple HTTP server using Python's built-in http.server
- CORS support
- Static file serving
