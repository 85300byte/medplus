import random
import string
import logging
import smtplib
import ssl
from email.mime.text import MIMEText
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)

def generate_otp():
    """Generate a 4-digit OTP"""
    return ''.join(random.choices(string.digits, k=4))

def send_otp_email(email, otp):
    """Send OTP via email"""
    subject = 'QuickMeds - Your Registration OTP'
    message = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuickMeds Registration OTP</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #4f46e5; text-align: center;">QuickMeds Registration</h2>
        <p>Hello,</p>
        <p>Thank you for registering with QuickMeds. Your One-Time Password (OTP) is:</p>
        <div style="background-color: #f3f4f6; padding: 15px; text-align: center; margin: 20px 0; border-radius: 5px;">
            <h1 style="color: #4f46e5; margin: 0; font-size: 32px; letter-spacing: 5px;">{otp}</h1>
        </div>
        <p><strong>Important:</strong></p>
        <ul>
            <li>This OTP will expire in 10 minutes</li>
            <li>Do not share this OTP with anyone</li>
            <li>If you didn't request this OTP, please ignore this email</li>
        </ul>
        <p>Best regards,<br>QuickMeds Team</p>
    </div>
</body>
</html>'''
    
    try:
        # Log attempt
        logger.info(f"Attempting to send OTP to {email}")
        
        # Print OTP for debugging
        print(f"\n{'='*50}")
        print(f"Attempting to send OTP {otp} to {email}")
        print(f"{'='*50}\n")
        
        # Create message with HTML content
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = f'QuickMeds <{settings.EMAIL_HOST_USER}>'
        msg['To'] = email
        msg['Reply-To'] = settings.EMAIL_HOST_USER
        msg['List-Unsubscribe'] = f'<mailto:{settings.EMAIL_HOST_USER}>'
        
        # Create SSL context
        context = ssl.create_default_context()
        
        # Connect to SMTP server using SSL
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as server:
            # Login
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            
            # Send email
            server.send_message(msg)
            
            logger.info(f"Successfully sent OTP to {email}")
            print(f"OTP sent successfully to {email}")
            return True
            
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"SMTP Authentication Error: {str(e)}")
        print(f"SMTP Authentication Error: {str(e)}")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP Error: {str(e)}")
        print(f"SMTP Error: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Error sending OTP to {email}: {str(e)}")
        print(f"\nError sending OTP: {str(e)}")
        return False

def store_otp(email, otp):
    """Store OTP in cache with 10 minutes expiration"""
    try:
        cache_key = f'otp_{email}'
        cache.set(cache_key, otp, timeout=600)  # 600 seconds = 10 minutes
        logger.info(f"OTP stored in cache for {email}")
        return True
    except Exception as e:
        logger.error(f"Failed to store OTP for {email}: {str(e)}")
        return False

def verify_otp(email, otp):
    """Verify OTP from cache"""
    try:
        cache_key = f'otp_{email}'
        stored_otp = cache.get(cache_key)
        
        if stored_otp and stored_otp == otp:
            cache.delete(cache_key)  # Delete OTP after successful verification
            logger.info(f"OTP verified successfully for {email}")
            return True
            
        logger.warning(f"Invalid OTP attempt for {email}")
        return False
        
    except Exception as e:
        logger.error(f"Error during OTP verification for {email}: {str(e)}")
        return False 