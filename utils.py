

def generate_regex(word_arr, additional=[], max_length=5):
    if word_arr is None:
        return None
    elif len(word_arr) != max_length:
        return None

    regex_list = ['(?=']
    regex = ''

    for i in range(5):
        if word_arr[i] and '-' not in word_arr[i]:
            regex_list.append(word_arr[i])
        else:
            regex_list.append('[a-z]{1}')

    regex_list.append(')')

    for a in additional:
        regex_list.append('(?=')
        regex_list.append('.*{}.*'.format(a))
        regex_list.append(')')

    print(regex.join(regex_list))
    return regex.join(regex_list)


def create_filter(regex):
    word_filter = {
        '$and': [
            {
                'madde': {
                    '$regex': regex
                }
            }, {
                'cesit': '0'
            }, {
                '$expr': {
                    '$eq': [
                        {
                            '$strLenCP': '$madde'
                        }, 5
                    ]
                }
            }
        ]
    }

    return word_filter
