'''集合覆盖问题，使用近似算法解决'''
# 创建一个列表，其中包含要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# 集合类似于列表，只是同样的元素只能出现一次

# 可供选择的广播台清单，选择使用散列表来表示它
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 使用一个集合来存储最终选择的广播台
final_stations = set()

# 遍历所有广播台，从中选择覆盖了最多的未覆盖州的广播台，将其存储在best_stations中
while states_needed:
    best_station = None
    states_covered = set() # states_covered是一个集合，包含该广播台覆盖的所有未覆盖的州
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 计算交集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)