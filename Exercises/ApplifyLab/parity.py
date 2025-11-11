val = input("")
arr = val.split()  # if i use split(" ") it will not work for input 0 0 0
new_list = []

for item in arr:
    if int(item) & 1 == 0:
        new_list.append("0")
    else:
        new_list.append("1")

ans = "".join(new_list).lstrip("0")  # remove leading zeros
print(ans or "0")
