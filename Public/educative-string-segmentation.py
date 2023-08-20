# dic = {
#     "apple": 1,
#     "pear": 1,
#     "pier": 1,
#     "pie": 1,
# }
dic = {
    "hello": 1,
    "hell": 1,
    "on": 1,
    "now": 1,
}


def check(s: str) -> bool:
    print(s)
    for i in range(len(s)):
        if s[: i + 1] in dic:
            if i + 1 == len(s) or check(s[i + 1 :]) == True:
                return True

    return False


# ex1 = "applepie"
# print(check(ex1))

ex1 = "hellonow"
print(check(ex1))

# ex2 = "applepeer"
# print(check(ex2))
