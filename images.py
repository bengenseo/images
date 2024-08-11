# 读取图片文件
with open("logo.png", "rb") as image_file:
    # 将图片转换为十六进制字符串
    hex_string = image_file.read().hex()
    logo="https://images.sjooo.sbs/logo.png"
print(hex_string)
