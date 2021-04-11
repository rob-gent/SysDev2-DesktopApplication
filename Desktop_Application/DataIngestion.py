import requests
import datetime

uri = 'http://localhost:8080'

todays_date = datetime.datetime.today().isoformat()[0:10]

print("Today is ", todays_date)

firstname = "1"
surname = "2"

params = {'First Name':firstname,'Last Name':surname}

r = requests.get(uri, params=params)

print("\nFirst Name " + firstname)
print("\nSurname " + surname)
print("\n-------------")

# To see the status code, print r
print(r)
#
#To see the return data, or error message, print r.text
print(r.text)

# if r:
#     t = r.json()
#     # near_earth_objects is a dictionary
#     for a in t['near_earth_objects']:
#         print(a)
#         objs = t['near_earth_objects'][a]
#         for obj in objs:
#             print("  id:", obj['id'], "  name:", obj['name'])
#             close_approach = obj['close_approach_data'][0]
#             print("  close approach date", close_approach['close_approach_date_full'])
#             print("  miss_distance", close_approach['miss_distance']['kilometers'],"km")