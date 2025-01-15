import smtplib
import pywhatkit
import time

def send_email():
    sender_email = input("আপনার জিমেইল অ্যাড্রেস দিন: ")
    sender_password = input("আপনার জিমেইল পাসওয়ার্ড দিন: ")
    receiver_email = input("যে জিমেইলে মেসেজ পাঠাতে চান: ")
    message = input("আপনার মেসেজ লিখুন: ")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
            print("ইমেইল সফলভাবে পাঠানো হয়েছে!")
    except Exception as e:
        print(f"একটি সমস্যা হয়েছে: {e}")

def send_message():
    number = input("যে নাম্বারে মেসেজ পাঠাতে চান (+880XXXXXXXXXX): ")
    message = input("আপনার মেসেজ লিখুন: ")
    hour = int(input("ঘণ্টা (২৪ ঘণ্টার ফরম্যাট): "))
    minute = int(input("মিনিট: "))

    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print("মেসেজ সফলভাবে পাঠানো হয়েছে!")
    except Exception as e:
        print(f"একটি সমস্যা হয়েছে: {e}")

def main():
    print("মেসেজ টুলস\n")
    print("১. জিমেইলে মেসেজ পাঠান")
    print("২. মোবাইল নাম্বারে মেসেজ পাঠান (WhatsApp)")
    choice = input("আপনার পছন্দ দিন (১/২): ")

    if choice == '১':
        send_email()
    elif choice == '২':
        send_message()
    else:
        print("ভুল পছন্দ, আবার চেষ্টা করুন!")

if __name__ == "__main__":
    main()
