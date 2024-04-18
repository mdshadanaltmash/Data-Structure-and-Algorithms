# Enter your code here. Read input from STDIN. Print output to STDOUT
heap = []


def min_val():
    return heap[0]


def insert_val(val: int):
    heap.append(val)
    heapify_up(len(heap) - 1)


def heapify_up(index):
    parent_idx = (index - 1) // 2
    while index != 0 and heap[parent_idx] > heap[index]:
        heap[parent_idx], heap[index] = heap[index], heap[parent_idx]
        index = parent_idx
        parent_idx = (index - 1) // 2


def delete_val(val: int):
    if val not in heap:
        return

    index = heap.index(val)
    if index == len(heap) - 1:
        heap.pop()
        return
    # parent = (index -1)//2
    heap[index] = heap[-1]
    heap.pop()

    heap_size = len(heap) - 1
    while index < len(heap) and len(heap) > 1:
        left_idx = (2 * index) + 1
        right_idx = (2 * index) + 2
        if left_idx <= heap_size:
            if right_idx <= heap_size:
                min_idx = left_idx if heap[left_idx]< heap[right_idx] else right_idx
            else:
                min_idx = left_idx
                if heap[index] > heap[min_idx]:
                    heap[index], heap[min_idx] = heap[min_idx], heap[index]
                break
            if heap[index] > heap[min_idx]:
                heap[index], heap[min_idx] = heap[min_idx], heap[index]
            else:
                break
            index = min_idx
        else:
            break


if __name__ == '__main__':
    # queries = int(input())
    inputs = ['1 4', '1 9', '1 10', '3', '2 9', '1 11', '1 13', '1 5', '1 7', '1 3', '2 7', '2 4', '3']
    inputs = ['1 286789035', '1 255653921', '1 274310529', '1 494521015', '3', '2 255653921', '2 286789035', '3',
              '1 236295092', '1 254828111', '2 254828111', '1 465995753', '1 85886315', '1 7959587', '1 20842598',
              '2 7959587', '3', '1 -51159108', '3', '2 -51159108', '3', '1 789534713']
    for opr_id in inputs:
        # opr_id = input()
        if opr_id == '3':
            print(min_val())
        elif opr_id.startswith('1'):
            insert_val(int(opr_id.split(' ')[1]))
        else:
            delete_val(int(opr_id.split(' ')[1]))
