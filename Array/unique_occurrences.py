def uniqueOccurrences(arr: [int]) -> bool:
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i,0) + 1

        a = []
        for key, value in hash_map.items():
            if value not in a:
                a.append(value)
            else:
                return False

        return True

a = [1,,2,2,1,1,3]

print(uniqueOccurrences(a))

def uniqueOccurrences1(arr: [int]) -> bool:
        return len(c := Counter(arr)) == len(set(c.values()))
