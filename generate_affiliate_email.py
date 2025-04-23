# generate_affiliate_email.py
import requests
import smtplib
from email.mime.text import MIMEText
from getpass import getpass  # Secure password input

# 1. Get AI-generated email (Hugging Face API)
def generate_email():
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {getpass('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: ')}"}
    prompt = "Write a 100-word marketing email for [Affiliate Product], with a CTA."
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()  # Raise error for bad status
        return response.json()[0]['generated_text']
    except Exception as e:
        print(f"⚠️ Error generating email: {e}")
        exit(1)

# 2. Send Email via Gmail SMTP
def send_email(content):
    sender_email = input("tinytawheedofficial@gmail.com: ")
    app_password = getpass("Farheen@12354: ")  # Never use plaintext password
    
    msg = MIMEText(content)
    msg['Subject'] = "🔥 Exclusive Affiliate Deal Inside!"
    msg['From'] = sender_email
    msg['To'] = input("Recipient email: ")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"⚠️ SMTP Error: {e}")

# Run the workflow
if __name__ == "__main__":
    email_content = generate_email()
    print("\nGenerated Email:\n" + "-"*50)
    print(email_content)
    send_email(email_content)
