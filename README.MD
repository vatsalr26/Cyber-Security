# VPTAA Authorization - OTP Verification System

## Overview
VPTAA Authorization is a secure OTP (One-Time Password) verification system designed for cybersecurity purposes. It allows users to log in using an OTP sent to their email, ensuring secure access to sensitive information.

## Features
- **OTP Generation**: A unique OTP is generated and sent to the user's email.
- **OTP Verification**: Users can verify the OTP to access a secure page.
- **Resend OTP**: Users can request a new OTP if the previous one expires.
- **Session Management**: Secure session handling with Flask.
- **Logout Functionality**: Users can log out and return to the login page.

## Prerequisites
- Python 3.11 or higher
- A Gmail account for sending OTPs (with App Password enabled)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vatsalr26/Cyber-Security.git
   cd vptaa-authorization
2. Create a virutal environment:
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
    pip install -r requirements.txt
4. Run the application:
    flask run