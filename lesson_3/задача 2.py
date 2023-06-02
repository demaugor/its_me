http_codes = {
  100: 'Continue',
  101: 'Switching Protocols',
  200: 'OK',
  201: 'Created',
  204: 'No Content',
  301: 'Moved Permanently',
  302: 'Found',
  304: 'Not Modified',
  400: 'Bad Request',
  401: 'Unauthorized',
  404: 'Not Found',
  500: 'Internal Server Error',
  502: 'Bad Gateway',
  504: 'Gateway Timeout',
  505: 'ай дурок я того не задавал'
}

max_1xx = 101
max_2xx = 204
max_3xx = 304
max_4xx = 404
max_5xx = 504

code = input("Введите http-код: ")

try:
    code = int(code)
    if 100 <= code <= 199:
        print(f"{code}: {http_codes[code]}")
        if code > max_1xx:
            print(f"\tНеизвестный код для группы 1xx: {code}")
        else:
            max_1xx = code
    elif 200 <= code <= 299:
        print(f"{code}: {http_codes[code]}")
        if code > max_2xx:
            print(f"\tНеизвестный код для группы 2xx: {code}")
        else:
            max_2xx = code
    elif 300 <= code <= 399:
        print(f"{code}: {http_codes[code]}")
        if code > max_3xx:
            print(f"\tНеизвестный код для группы 3xx: {code}")
        else:
            max_3xx = code
    elif 400 <= code <= 499:
        print(f"{code}: {http_codes[code]}")
        if code > max_4xx:
            print(f"\tНеизвестный код для группы 4xx: {code}")
        else:
            max_4xx = code
    elif 500 <= code <= 599:
        print(f"{code}: {http_codes[code]}")
        if code > max_5xx:
            print(f"\tНеизвестный код для группы 5xx: {code}")
        else:
            max_5xx = code
    else:
        print("Неизвестный http-код")
        
except ValueError:
    print("Ошибка: введено некорректное значение")