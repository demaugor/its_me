HttpCode = int(input("Введите http-код: "))

match HttpCode:
    case 100:
        print("Continue")
    case 102:
        print("Processing")
    case 103:
        print("Early Hints")
    case code1xx if HttpCode > 103 and HttpCode < 200:
        print("Неизвестный код для группы 1xx")
    case 200:
        print("OK")
    case 204:
        print("No Content")
    case code2xx if HttpCode > 207 and HttpCode < 300:
        print("Неизвестный код для группы 2xx")
    case 302:
        print("Found")
    case 305:
        print("Use Proxy")
    case code3xx if HttpCode > 308 and HttpCode < 400:
        print("Неизвестный код для группы 3xx")
    case 404:
        print("Not Found")
    case 409:
        print("Conflict")
    case code4xx if HttpCode > 409 and HttpCode < 500:
        print("Неизвестный код для группы 4xx")
    case 503:
        print("Service Unavailable")
    case 510:
        print("Not Extended")
    case code5xx if HttpCode > 511:
        print("Неизвестный код для группы 5xx")
    case _:
        print("Неизвестный код")