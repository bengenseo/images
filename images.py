import base64

with open("logo.ico", "rb") as icon_file:
    encoded_string = base64.b64encode(icon_file.read()).decode('utf-8')
    print(encoded_string)
