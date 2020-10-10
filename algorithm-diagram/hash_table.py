'''hash table 散列表的应用实例'''
# 1) 将散列表用于查找
phone_book = dict()
# ->phone_book = {}
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])

# 2) 防止重复
voted = {}
# value = voted.get("tom")

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")

check_voter("tom")
check_voter("mike")
check_voter("mike")

# 3）将散列表用作缓存
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data