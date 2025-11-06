# [expression for item in iterable if condition]
## 🧩 **LEVEL 1: Basics**

# Practice simple transformations and element extraction.

# 1. ✅ Generate a list of numbers from `1` to `10`.

ans = [i for i in range(1,11)]
# print(ans)

# 2. ✅ Create a list of their squares.
li = [3,2,4,1]
squares = [item**2 for item in li]
# print(squares)

# 3. ✅ Create a list of cubes for numbers from `1` to `5`.
li2 = [1,2,3,4,5]
cubes = [item**3 for item in li2]
# print(cubes)
# 4. ✅ Convert all characters in `"hello world"` to uppercase.
s = "hello world"
new_s_upper =[char.upper() for char in s]
new_s = "".join(new_s_upper)
# print(new_s)
# 5. ✅ Extract digits from a mixed string `"a1b2c3d4"`.
mixed_str = "a1b2c3d4"
digits = [digit for digit in mixed_str if digit.isdigit()]
print(digits)