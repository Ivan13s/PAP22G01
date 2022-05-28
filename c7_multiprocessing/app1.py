from multiprocessing import Process, Queue
import json
import time
import requests
import aiohttp


def time_zone_getter(location, cities: Queue):
    result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location}')
    # print(json.loads(result.text))
    cities.put(json.loads(result.text))


def time_getter(city: str):
    result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{city}')
    print(json.loads(result.text))


if __name__ == "__main__":
    processes = []
    cities = Queue()
    for location in ['europe', 'asia', 'america']:
        p = Process(target=time_zone_getter, args=(location, cities))
        processes.append(p)
    start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    # p1.start()
    # p1.join()
    stop = time.time()
    print('Time: ', stop-start)
    while not cities.empty():
        print(cities.get())
    # print(cities.get())
    # print(cities.empty())
    # print(cities.get())
    # print(cities.empty())
    # print(cities.get())
    # print(cities.empty())