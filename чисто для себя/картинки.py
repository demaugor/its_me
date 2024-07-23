def image_to_hex(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        return binary_data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except IOError:
        print(f"Error: Could not read the file {file_path}.")
        return None

def binary_to_hex(binary_data):
    if binary_data is None:
        return None
    return binary_data.hex()

# Пример использования
file_path = r'C:\\Users\demau\\Pictures\\Camera Roll\\kar.jpg'  # Используем сырой строковый литерал

binary_data = image_to_hex(file_path)

if binary_data is not None:
    hex_string = binary_to_hex(binary_data)
    print(hex_string[:1000])  # Выводим только первые 1000 символов, чтобы не перегружать консоль
else:
    print("Failed to convert image to hexadecimal string.")