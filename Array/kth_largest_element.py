
def find_kth_largest_element(arr:[int]) -> int:

    return sorted(arr, reverse=True)[k-1]


arr = [1,3,42,5,6,3,5,6,6]
k= 4

print(find_kth_largest_element(arr))