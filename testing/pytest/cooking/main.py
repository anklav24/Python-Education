# On 1000 g. meal
#
# A Nitro salt: 10
# A Usual salt: 15
# Starts culture: 0.5
# Mono-sugars: 5
# 2 days on every 500 g.

def nitro_salt(m):
    # 1000 : 10 = m : x
    # print(10 * m // 1000)
    try:
        m = int(m)
    except ValueError:
        m = 0
    return 10 * m // 1000


nitro_salt("qwerty")
