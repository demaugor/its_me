HttpCode = int(input("Введите http-код: "))
match HttpCode:
    
    case 100:
        print("Continue")
    case 102:
        print("Processing")
    case 103:
        print("Early Hints")
    case 200:
        print("Continue")
    case 204:
        print("Processing")
    case 302:
        print("Found")
    case 305:
        print("Use Proxy")
    case 404:
        print("Not Found")
    case 409:
        print("Conflict")
    case 503:
        print("Service Unavailable")
    case 510:
        print("Not Extended")
        
if HttpCode > 103:
    print("Неизвестный код для группы 1xx")
elif HttpCode > 207:
    print("Неизвестный код для группы 2xx")
elif HttpCode > 308:
    print("Неизвестный код для группы 3xx")
elif HttpCode > 499:
    print("Неизвестный код для группы 4xx")
elif HttpCode > 599:
    print("Неизвестный код для группы 5xx")