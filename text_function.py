import math


def separate_text(text):

    answer_list = []

    for _ in range(len(text)):
        if text:
            space_position = text[:1994][::-1].find(' ')

            if 0 <= space_position <= 500:
                answer_list.append('=> ' + text[:(1994 - (space_position + 1))] + ' =>')
                text = text[(1994 - (space_position)):]

            else:
                answer_list.append(text[:1994])
                text = text[1994:]

        else:
            answer_list[0] = answer_list[0][2:]
            answer_list[-1] = answer_list[-1][:-3]
            break

    return answer_list
