import requests
import json

#GET, veri alırken
#user_input = input("Enter id: ")
#get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

#get_response = requests.get(get_url)
#print(get_response.json())


#POST, veri yollarken (yeni veri eklemek, güncellemek)
to_do_item = {"userId": 2, "title": "my to do", "completed": False}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional header
headers = {"Content-Typw": "application/json"}
#post_response = requests.post(post_url, json=to_do_item, headers=headers) #json olarak yollamak.
post_response = requests.post(post_url, data=json.dumps(to_do_item), headers=headers) #data olarak çalıştırmak fakat json.dumps ile sözlüğü json'a çevirip.
print(post_response.json())
#print(json.dumps(to_do_item)) #bu bir json oldu. json.dumps ile bunu sözlük değil json halinde post attık.