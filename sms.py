import requests

def send_sms(number, message):
    url = 'https://api.my1freehosting.com/SendSMS.php'
    payload = {
        'Phone': number,
        'Message': message,
    }
    response = requests.post(url, data=payload)
    return response.text

if __name__ == '__main__':
    number = input('Enter the phone number: ')
    message = input('Enter the message: ')
    response = send_sms(number, message)
    print('Response:', response)
