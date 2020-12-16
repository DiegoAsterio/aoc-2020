import math
import pdb

def load_timestamps(path):
    with open(path) as f:
        inp = f.read().strip().split('\n')
    arrival = int(inp[0])
    buses = [int(x) for x in inp[1].split(',') if x != 'x']
    return arrival, buses

def earliest_departure(arrival, buses):
    departure = math.inf
    earliest_bus = None 
    for bus in buses:
        q = arrival//bus
        r = arrival % bus
        if r != 0:
            q += 1
        if q*bus < departure:
            departure = q*bus
            earliest_bus = bus
    return earliest_bus, departure

if __name__ == "__main__":
    path = "2020_12_12.input"
    arrival, buses = load_timestamps(path)
    bus_id, departure = earliest_departure(arrival, buses)
    minutes_waiting = departure - arrival

    print("The ID of the bus times minutes waiting is {}".format(bus_id*minutes_waiting))
