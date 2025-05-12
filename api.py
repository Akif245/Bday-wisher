import requests

response=requests.get(url="https://annafifoundation.com/")
response.raise_for_status()

data=response.json()

longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]

iss_position=(longitude,longitude)
print(iss_position)






# print(response)
# if response.status_code!=200:
#     print("Error")
# else:
#     print("Success!")
