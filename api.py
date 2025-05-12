import requests

response=requests.get("https://annafifoundation.com/")
# print(response)
if response.status_code!=200:
    print("Error")
else:
    print("Success!")