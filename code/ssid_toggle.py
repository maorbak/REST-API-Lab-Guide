""" Enable/Disable Wifi on a Meraki Network """

import requests

# ****** START EDIT THIS ******

api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"  # Replace with your API key
network_id = "L_646829496481105433"  # Replace with your Network ID
ssid_number = "1"  # Replace with your ssid number to edit

# ****** STOP EDIT THIS  ******

url = "https://api.meraki.com/api/v0/networks/{}/ssids/{}".format(
    network_id, ssid_number
)

headers = {"X-Cisco-Meraki-API-Key": api_key}
payload = {
    "name": "Mari's Wifi",
    "enabled": "true",
}

response = requests.request("PUT", url, data=payload, headers=headers)

print("\nAPI Response: \n{}".format(response.text))
print("\nStatus code: {}".format(response.status_code))
