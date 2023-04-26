from plyer import notification # make notification
import requests # get info
import time # wait
import datetime # get time

# limits
cpu_limit = 80
memory_limit = 80


def make_notification(name, number, address):
    time = datetime.datetime.now() # get current time
    time_formated = time.strftime("%Y-%m-%d %H:%M") # time in right format

    notification.notify( #make notification
        title=f'{name} usage over limit',
        message=f'PC {address} {time_formated}:{name} usage {number}.',
        app_name='Allert app',
        timeout=10
)


def main():
    address_list = ["192.168.71.103:8000", "192.168.71.104:8000"] # list of monitored deviced
    while (True):
        for address in address_list:
            try:
                # get info
                response1 = requests.get(f"http://{address}/cpu", timeout=1)
                response2 = requests.get(f"http://{address}/memory", timeout=1)
                cpu = int(response1.json())
                memory = int(response2.json())

                # make notification if over limit
                if cpu > cpu_limit:
                    make_notification("Cpu", cpu, address)
                if memory > memory_limit:
                    make_notification("Memory", memory, address)
                    
            except requests.exceptions.RequestException as e:
                print("Error making API call:", e)

        time.sleep(60) # wait
    
main()


