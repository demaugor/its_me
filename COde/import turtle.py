def con(lst):
    ref = []
    for word in lst:
        reserved_ref = word[::-1]
        ref.append(reserved_ref)
    return  ref

ref = ["литература", "музыка"]
print(con(ref))
