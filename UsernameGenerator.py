import requests
import json
import string
import random
NOU = int(input('Number Of Usernames You Want To Generate : '))
NOL = int(input('Number Of Letters You Want : '))
def Generate():
    username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(NOL))
    api = f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1982-08-08"
    r = requests.get(api).json()
    if r ['code'] != 0:
        print(username, '(Invalid!)')
    else:
        print(username, '(Valid!)')

for i in range(NOU):
    Generate()