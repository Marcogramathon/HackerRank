# import requests module
import requests
 
# Making a get request
response = requests.get('https://api.chucknorris.io/jokes/random')
 
# Store JSON data in API_Data
API_Data = response.json()
 
# Print json data using loop
for key in API_Data:
    print(key,":", API_Data[key])

print('------>', API_Data['id'])