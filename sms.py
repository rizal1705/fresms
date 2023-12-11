import requests

def send_sms(number, message):
    url = 'https://freesms.telzir.com/webservice/sms.php'
    payload = {
        'to': number,
        'msg': message,
    }
    response = requests.post(url, data=payload)
    return response.text

if __name__ == '__main__':
    number = input('Enter the phone number: ')
    message = input('Enter the message: ')
    response = send_sms(number, message)
    print('Response:', response)
