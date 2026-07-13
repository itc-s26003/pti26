def posttaxprice(price):
    ans = price * 1.08
    return int(ans)

print(posttaxprice(120),"円")
print(posttaxprice(128),"円")
print(posttaxprice(980),"円")
