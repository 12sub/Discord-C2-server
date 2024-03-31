import requests
import sys
import logging

discovered_subdoamins = []



sub_lists = open("subdomains.txt").read()
subdomain = sub_lists.splitlines()


for subways in subdomain:
    sub_domains = f"https://{subways}.{sys.argv[1]}/"
    try:
        req = requests.get(sub_domains)
        
    except requests.ConnectionError:
        pass
    else:
        print("Valid Domain:", sub_domains)
        discovered_subdoamins.append(sub_domains)

with open("discovered_subdoamins.txt", "w") as f:
    for subdomain in discovered_subdoamins:
        print(subdomain, file=f)    