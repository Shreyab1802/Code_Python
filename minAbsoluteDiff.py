def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr = sorted(arr)
    min_diff = sys.maxsize - 1
    dictDiff = {}
    result = []

    for i in range(len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        min_diff = min(min_diff, diff)
        print(diff)

    for i in range(len(arr) - 1):
        if (arr[i + 1] - arr[i] == min_diff):
            result.append([arr[i], arr[i + 1]])

    return result