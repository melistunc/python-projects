from unittest.mock import patch

import requests

from mainn import to_do_item

get_url = "https://jsonplaceholder.typicode.com/todos/14"

get_response = requests.get(get_url)
print(get_response.json())

#PUT ,bir satırı tamamen değiştirmek gibidir. Burası fake gibi değiştirir.
to_do_item_14 = {"userId" : 4, "title": "put title", "completed": False}
put_response = requests.put(get_url, json=to_do_item_15)
print(put_response.json())


#PATCH ,satırın sadece bir kısmını değiştirir.
to_do_item_patch_14 = {"title": "Patch test"}
patch_response = requests.patch(get_url, json=to_do_item_patch_14)
print(patch_response.json())

#DELETE ,komple satırı siler.
delete_response = requests.delete(get_url)
print(delete_response.json()) #ekrana boş çıktı verir.