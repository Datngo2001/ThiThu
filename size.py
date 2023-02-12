# %% [markdown]
# Đọc File

# %%
input = ""

with open('size.inp', 'r') as fi:
    input = fi.read()

# %% [markdown]
# Tách data thành các cặp chiều cao và cân nặng

# %%
height_and_weight_list = input.split("\n")
print(height_and_weight_list)

# %% [markdown]
# Tạo File size.out

# %%
file_out = open("size.out", "x")

# %% [markdown]
# Kiểm tra điều kiện và viết kết quả vào file

# %%
for height_and_weight in height_and_weight_list:
    [height, weight] = height_and_weight.split(" ")
    height = float(height)
    weight = int(weight)
    if (1.6 <= height <= 1.65) & (55 <= weight <= 60):
        file_out.write("S\n")
    elif (1.66 <= height <= 1.69) & (60 <= weight <= 65):
        file_out.write("M\n")
    elif (1.70 <= height <= 1.74) & (66 <= weight <= 70):
        file_out.write("L\n")
    elif (1.75 <= height <= 1.76) & (70 <= weight <= 76):
        file_out.write("XL\n")
    elif (1.75 <= height <= 1.77) & (76 <= weight <= 80):
        file_out.write("XXL\n")
    else:
        file_out.write("NO\n")


# %% [markdown]
# Đóng File

# %%
file_out.close()
