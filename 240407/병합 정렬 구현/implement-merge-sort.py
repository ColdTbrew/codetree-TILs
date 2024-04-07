def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    merged_arr = [0] * (high - low + 1)  # merged_arr 리스트 초기화
    i, j, k = low, mid + 1, 0  # k는 merged_arr의 인덱스로 사용
    while(i<= mid and j <= high):
        if arr[i] < arr[j]:
            merged_arr[k] = arr[i];
            k+= 1
            i +=1
        else:
            merged_arr[k] = arr[j];
            k+=1
            j+= 1
    while(i<= mid):
        merged_arr[k] = arr[i];
        k+= 1
        i +=1
    while(j<= high):
        merged_arr[k] = arr[j];
        k+=1
        j+= 1

    for idx, val in enumerate(merged_arr):
        arr[low + idx] = val 

    return arr

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr, 0, n-1)

print(" ".join(map(str, arr)))