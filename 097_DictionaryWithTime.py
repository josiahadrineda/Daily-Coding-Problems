from bisect import bisect_left

class Map:
    def __init__(self):
        self.key_to_time_to_value = {}

    # O(log(n))
    def __repr__(self):
        # Print values in chronological order
        if self.key_to_time_to_value:
            for key, time_value in sorted(self.key_to_time_to_value.items()):
                print(f'Key {key}')
                for time, value in sorted(time_value.items()):
                    print(f'\tValue {value} set @ Time {time}')
            return ''
        return 'No values to be logged.'

    # O(1)
    def set(self, key, value, time):
        if self.key_to_time_to_value.get(key):
            self.key_to_time_to_value[key][time] = value
        else:
            self.key_to_time_to_value[key] = {}
            self.key_to_time_to_value[key][time] = value

    # O(log(n))
    def get(self, key, time):
        if self.key_to_time_to_value.get(key):
            timeline = sorted(self.key_to_time_to_value[key])
            timestamp_ind = bisect_left(timeline, time)
            if 0 <= timestamp_ind < len(timeline) and timeline[timestamp_ind] == time:
                return self.key_to_time_to_value[key][time]
            elif 0 <= timestamp_ind - 1 < len(timeline):
                return self.key_to_time_to_value[key][timeline[timestamp_ind - 1]]

map = Map()
assert map.set(1,1,0) == None
assert map.set(1,2,2) == None
assert map.get(1,1) == 1
assert map.get(1,3) == 2
print(map)

map = Map()
assert map.set(1,1,5) == None
assert map.get(1,0) == None
assert map.get(1,10) == 1
print(map)

map = Map()
assert map.set(1,1,0) == None
assert map.set(1,2,0) == None
assert map.get(1,0) == 2
print(map)


from bisect import bisect

class CleanerMap:
    def __init__(self):
        self.map = {}

    # O(1)
    def __repr__(self):
        return str(self.map)

    # O(log(n))
    def set(self, key, value, time):
        if not self.map.get(key):
            self.map[key] = ([value], [time])
            return

        values, times = self.map[key]
        insertion_ind = bisect(times, time)
        
        values.insert(insertion_ind, value)
        times.insert(insertion_ind, time)

    # O(log(n))
    def get(self, key, time):
        if not self.map.get(key):
            return

        values, times = self.map[key]
        insertion_ind = bisect(times, time)

        if insertion_ind:
            return values[insertion_ind - 1]

map = CleanerMap()
assert map.set(1,1,0) == None
assert map.set(1,2,2) == None
assert map.get(1,1) == 1
assert map.get(1,3) == 2
print(map)

map = CleanerMap()
assert map.set(1,1,5) == None
assert map.get(1,0) == None
assert map.get(1,10) == 1
print(map)

map = CleanerMap()
assert map.set(1,1,0) == None
assert map.set(1,2,0) == None
assert map.get(1,0) == 2
print(map)