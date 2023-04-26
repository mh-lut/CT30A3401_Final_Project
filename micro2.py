import requests # get info from api
import time # wait
import pymongo # database use
import datetime # current time

def mongo(cpu_value, memory_value, address):
    # connecto to the database server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # select database
    db = client["pc_usage_dp"]

    # select the collection you want to work with
    collection = db[address]

    # insert info into the collection
    info = {"cpu": str(cpu_value), "menory": str(memory_value), "time": str(datetime.datetime.now())}
    collection.insert_one(info)




def main():
    address_list = ["192.168.71.103:8000", "192.168.71.104:8000"] # list of monitored deviced
    while (True):
        for address in address_list:
            try:
                # get info
                response1 = requests.get(f"http://{address}/cpu", timeout=1)
                response2 = requests.get(f"http://{address}/memory", timeout=1)

                mongo(response1.json(), response2, address) # put info to database
            except requests.exceptions.RequestException as e: # if error
                print("Error making API call:", e)

        time.sleep(60) # wait 60s
    
main()