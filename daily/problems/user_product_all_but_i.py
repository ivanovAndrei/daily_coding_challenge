"""Given an array, return a new array where each element at index i is product 
all original array elements except at ith index"""

def _product_array_no_division(input:list)->list:
    output = list()
    for i in range(len(input)):
        product = 1
        for j in range(len(input)):
            product = product * input[j] if i != j else product
        output.append(product)
    return output

def _product_list_division(input:list)->list:
    output=list()
    total_product = 1
    for i in input:
        total_product = total_product * i
    
    for i in range(len(input)):
        output.append(total_product/input[i] if input[i] != 0 else 0)

    return output

output_nodiv_1 = _product_array_no_division([3, 2, 1])
print(output_nodiv_1)
output_nodiv_2 = _product_array_no_division([1,2,3,4,5])
print(output_nodiv_2)

output_div_1 = _product_list_division([3,2,1])
assert output_div_1 == output_nodiv_1
output_div_2 = _product_list_division([1,2,3,4,5])
assert output_div_2 == output_nodiv_2