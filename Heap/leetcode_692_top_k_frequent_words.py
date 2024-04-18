class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        heap = []
        checked = {}
        for word in words:
            heap = self.insert_into_heap(heap, word, checked)
        print(heap)
        # return [heap[i][0] for i in range(k)]
        res = []
        while k:
            k -= 1
            heap, result = self.pop_max_from_heap(heap)
            res.append(result)
        return res

    def insert_into_heap(self, heap, word, checked):
        if word not in checked:
            checked[word] = 1
            heap.append([word, 1])
            if len(heap) == 0:
                return
            return self.heapify(heap, len(heap) - 1)
        else:
            word_count = checked[word]
            index = heap.index([word, word_count])
            heap[index] = [word, word_count + 1]
            checked[word] = word_count + 1
            return self.heapify(heap, index)

    def heapify(self, heap, index):
        parent_idx = (index - 1) // 2
        while index != 0:
            if heap[parent_idx][1] < heap[index][1]:
                heap[parent_idx], heap[index] = heap[index], heap[parent_idx]
            elif heap[parent_idx][1] == heap[index][1]:
                if heap[parent_idx][0] > heap[index][0]:
                    heap[parent_idx], heap[index] = heap[index], heap[parent_idx]
                else:
                    break
            else:
                break
            index = parent_idx
            parent_idx = (index - 1) // 2
        return heap

    def pop_max_from_heap(self, heap):
        op = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        heap_size = len(heap) - 1
        curr = 0

        def swap(curr, min_child):
            if heap[curr][1] < heap[min_child][1]:
                heap[curr], heap[min_child] = heap[min_child], heap[curr]
            elif heap[curr][1] == heap[min_child][1]:
                if heap[curr][0] > heap[min_child][0]:
                    heap[curr], heap[min_child] = heap[min_child], heap[curr]

        while curr < heap_size:
            l = (2 * curr) + 1
            r = (2 * curr) + 2
            if l > heap_size:
                break
            if r > heap_size:
                if self.get_max_index(heap, curr, l) == l:
                    swap(curr, l)
                break

            min_child = self.get_max_index(heap, l, r)
            swap(curr, min_child)
            curr = min_child
        return heap, op[0]

    def get_max_index(self, heap, l, r) -> int:
        if heap[l][1] > heap[r][1]:
            return l
        elif heap[l][1] < heap[r][1]:
            return r
        else:
            return l if heap[l][0] < heap[r][0] else r


obj = Solution()
# ip = ["i", "love", "leetcode", "i", "love", "coding"]
ip = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(obj.topKFrequent(ip, k))
