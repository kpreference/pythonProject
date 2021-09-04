while True:
    try:
        a, b = map(float, input().split())
        print("%.2f" % (a / b))
    except:
        break