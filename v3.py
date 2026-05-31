from v2 import TextSystemV2

# V3版本：新增冒泡排序、KMP算法、BF与KMP效率对比
class TextSystemV3(TextSystemV2):
    def __init__(self):
        super().__init__()

    # 冒泡排序
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # BF暴力匹配
    def bf_search(self, text, pattern):
        n = len(text)
        m = len(pattern)
        for i in range(n - m + 1):
            j = 0
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                return i
        return -1

    # KMP算法
    def kmp_search(self, text, pattern):
        def get_next(pat):
            m = len(pat)
            nxt = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pat[i] != pat[j]:
                    j = nxt[j - 1]
                if pat[i] == pat[j]:
                    j += 1
                nxt[i] = j
            return nxt

        nxt = get_next(pattern)
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = nxt[j - 1]
            if text[i] == pattern[j]:
                j += 1
            if j == len(pattern):
                return i - j + 1
        return -1
