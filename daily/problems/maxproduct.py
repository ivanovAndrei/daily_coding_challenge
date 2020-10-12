def max_product(inputstr:str)->int:
    try:
        assert len(inputstr) >= 4, "String should be at least 4 characters long"
        # num_slices guarantees that we're only considering the 4 digit strings.
        num_slices = len(inputstr)-3
        max_product = 0 
        for i in range(0, num_slices):
            substr = inputstr[i:i+4]
            print(substr)
            a, b, c, d = substr
            product = int(a) * int(b) * int(c) * int(d)
            max_product = product if product > max_product else max_product
    except Exception as exc:
        print(exc)

    return max_product

max_product("1a3456789")
