# 读取图片文件
with open("images.png", "rb") as image_file:
    # 将图片转换为十六进制字符串
    hex_string = image_file.read().hex()

print(hex_string)
