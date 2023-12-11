import requests

def send_sms(number, message):
    url = 'https://websms.shoutpoint.com/websmsapi/v1.0/send.jsp'
    payload = {
        'phone': number,
        'message': message,
        'mtype': 'sms'
    }
    response = requests.post(url, data=payload)
    return response.text

if __name__ == '__main__':
    number = input('Enter the phone number: ')
    message = input('Enter the message: ')
    response = send_sms(number, message)
    print('Response:', response)
