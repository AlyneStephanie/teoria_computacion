def is_even(s):

    # SHORT VERSION
    # return  s.count('1') % 2 == 0

    # LONG VERSION
    state = 'q0'

    for c in s:
        match c:
            case '0':
                match state:
                    case 'q0':
                        state = 'q1'
                    case 'q1':
                        state = 'q0'
                    case 'q2':
                        state = 'q3'
                    case 'q3':
                        state = 'q2'
            case '1':
                match state:
                    case 'q0':
                        state = 'q2'
                    case 'q2':
                        state = 'q0'
                    case 'q1':
                        state = 'q3'
                    case 'q3':
                        state = 'q1'

    match state:
        case 'q0':
            return True
        case 'q1':
            return False

def main():
    print(is_even('0011'))

if __name__ == '__main__':
    main()