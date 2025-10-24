def letter(poem):
    ans = {}
    for l in poem:
        if l not in tuple(ans.keys()):
            ans[l] = 1
        else:
            ans[l] += 1
    return ans

poem = "Зайку бросила хозяйка -- Под дождем остался зайка. Со скамейки слезть не мог, Весь до ниточки промок."
rez = letter(poem)
print("В строке %s:" % poem)
for key in list(rez.keys()):
    print(f"{rez[key]} символов {key}")