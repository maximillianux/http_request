import requests
import hashlib
filename = 'request_file.txt'

def request():
    http = 'https://www.google.com/'
    request = requests.get(http)
    with open(filename, 'w') as file:
        file.write(request.text)
    checksum()

def checksum():
    with open(filename) as openfile:
        data = openfile.read()
        sum = hashlib.md5(data.encode('utf-8')).hexdigest()
    with open('checksum.md5', 'w') as check:
        check.write(sum)

if __name__=="__main__":
    request()