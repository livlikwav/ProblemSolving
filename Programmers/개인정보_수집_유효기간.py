def solution(today, terms, privacies):  # terms max=20, privacies max=100
    """
    Voted #1 아 이렇게 간단한 수학적 아이디어를 쓰니까 훨씬 간단하네;;
    Day 기준으로 YY, MM 도 그냥 int 값으로 치환해서, 비교하니까 편하다.
    만약 Day 연산이 있었으면 28 넘어가면 자리 올림 처리를 해줘야해서 복잡했겠지만,
    이거 YY, MM 계산만 있으니 이렇게 할 수 있다. 좋은 아이디어!!
    """
    def to_days(date):
        y, m, d = map(int, date.split(".")
        return y * 28 * 12 + m * 28 + d
    
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
    """
    MY SOLUTION
    """
    ty, tm, td = map(int, today.split("."))

    termd = {}
    for term in terms:  # O(20)
        name, s = term.split()
        val = int(s)
        termd[name] = val

    result = []
    for i in range(len(privacies)):  # O(100)
        date, name = privacies[i].split()
        y, m, nd = map(int, date.split("."))

        target_month = termd[name]
        nm, ny = -1, -1
        if (m + target_month) % 12 == 0:
            nm = 12
            ny = y + (m + target_month) // 12 - 1
        else:
            nm = (m + target_month) % 12
            ny = y + (m + target_month) // 12

        # check expiry
        if ty < ny:
            continue
        elif ny < ty:
            result.append(i + 1)
            continue
        else:  # same year
            if tm < nm:
                continue
            elif nm < tm:
                result.append(i + 1)
                continue
            elif td >= nd:  # same month
                result.append(i + 1)
                continue

    return result
