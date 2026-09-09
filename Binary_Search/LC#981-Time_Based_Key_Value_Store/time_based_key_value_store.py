# 981. Time Based Key-Value Store
# Difficulty: Medium
# Topics: Hash Table, String, Binary Search, Design
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values_list = self.map[key]
        # binary search to find timestamp since values are sorted
        l = 0
        r = len(values_list) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            mid_timestamp, mid_value = self.map[key][mid]
            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp > timestamp:
                r = mid - 1
            else:
                result = mid_value
                l = mid + 1
        return result

solution_1_instance = TimeMap()
solution_1_instance.set("foo", "bar", 1)
assert solution_1_instance.get("foo", 1) == "bar"
assert solution_1_instance.get("foo", 3) == "bar"

solution_1_instance.set("foo", "bar2", 4)
assert solution_1_instance.get("foo", 4) == "bar2"
assert solution_1_instance.get("foo", 5) == "bar2"

print("All tests passed successfully!")

