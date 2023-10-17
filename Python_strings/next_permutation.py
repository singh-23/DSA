class Solution:
    def nextPermutation(self, N, arr):
        j = -1;
        i = N - 1;
        while (i >= 0):
            if arr[i] > arr[i - 1]:
                j = i - 1;
                break;
            i = i - 1;
        i = N - 1;
        if j != -1:
            while (i >= 0):
                if arr[i] > arr[j]:
                    tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                    break;
                i = i - 1;

        j = j + 1;
        i = N - 1;
        while j <= i:
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            j = j + 1;
            i = i - 1;

        return arr;