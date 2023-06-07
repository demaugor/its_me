Http_Code = int(input("Введите http_код: "))

match Http_Code:
    
    case 100:
        print("Continue")
    case 102:
        print("Processing")
    case 103:
        print("Early Hints")
    case code1xx if Http_Code > 103 and Http_Code < 200:
        print("Неизвестный код для группы 1xx")
            
    case 200:
        print("OK")
    case 203:
        print ("Non-Authoritative")
    case 204:
        print("No content")
    case 207:
        print("Multi-Status")
    case code2xx  if Http_Code > 207 and Http_Code < 300:
        print("Неизвестный код для группы 2xx")
            
    case 300:
        print("Move Choices")
    case 302:
        print("Found")
    case 305:
        print("Use Proxy")
    case code3xx if Http_Code > 308 and Http_Code < 400:
        print("Неизвестный код для группы 3xx")
            
    case 404:
        print("Not Found")
    case 409:
        print("Conflict")
    case ode4xx if Http_Code > 409 and Http_Code < 500:
        print("Неизвестный код для группы 4xx")
        
    case 503:
        print("Service Unavailable")
    case 509:
        print("Bandwidth Limit Exceeded")
    case 510:
        print("Not Extended")
    case code5xx if Http_Code > 510:
        print("Неизвестный код для группы 5xx")
    
    case _:
        print("неизвестный Http_Code")