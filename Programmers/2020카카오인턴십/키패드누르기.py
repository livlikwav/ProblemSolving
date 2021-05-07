'''
28분 걸림.
좀 헤맨편인듯..? global 설정하는것 때문에.
왼손 오른손 위치를 업데이트 해주는 것을 잘 케이스를 나눠서 바로 했어야 됐다!
'''
position = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    '*': (3, 0),
    0: (3, 1),
    '#': (3, 2)
}
left_hand = position['*']
right_hand = position['#']

def solution(numbers, hand):
    global left_hand
    global right_hand

    def comp_hands(num: int) -> str:
        global left_hand
        global right_hand

        left_hand[0]

        num_position = position[num]

        left_distance = abs(num_position[0]- left_hand[0]) + abs(num_position[1] - left_hand[1])
        right_distance = abs(num_position[0] - right_hand[0]) + abs(num_position[1] - right_hand[1])

        if left_distance < right_distance:
            left_hand = position[num]
            return 'L'
        elif left_distance > right_distance:
            right_hand = position[num]
            return 'R'
        else:
            if hand == 'right':
                right_hand = position[num]
                return 'R'
            else:
                left_hand = position[num]
                return 'L'

    mapping = {
        1: 'L',
        4: 'L',
        7: 'L',
        3: 'R',
        6: 'R',
        9: 'R',
    }

    result = ''

    for num in numbers:
        if num in mapping:
            val = mapping[num]
            result += val
            if val == 'L':
                left_hand = position[num]
            else:
                right_hand = position[num]
        else:
            result += comp_hands(num)
            
    return result

# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
# solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")