def get_rem_product(arr: [int]) -> list[int]:
    prefix_products = []
    for num in arr:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products = []
    for num in reversed(arr):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    result = []
    # print(prefix_products)
    # print(suffix_products)
    for i in range(len(arr)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(arr)-1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1]*suffix_products[i+1])
    return result


arr = [1, 2, 3, 4, 5]
print(get_rem_product(arr))
