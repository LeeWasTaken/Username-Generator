import requests
import json
import string
import random
NOU =int (input ('Number Of Usernames You Want To Generate : '))
NOL =int (input ('Number Of Letters You Want : '))
def Generate ():
    O0O000OOOO0OOO000 =''.join (random .choice (string .ascii_letters +string .digits )for O00O0O00OOO0000OO in range (NOL ))
    OO00O0OOO00OO000O =f"https://auth.roblox.com/v1/usernames/validate?request.username={O0O000OOOO0OOO000}&request.birthday=1982-08-08"
    O00000OOO00OOOOOO =requests .get (OO00O0OOO00OO000O ).json ()
    if O00000OOO00OOOOOO ['code']!=0 :
        print (O0O000OOOO0OOO000 ,'(Invalid!)')
    else :
        print (O0O000OOOO0OOO000 ,'(Valid!)')
for i in range (NOU ):
    Generate ()
