def calculate(a, op, b):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else None,
    }
    if op not in ops:
        return None, f'지원하지 않는 연산자: {op}'
    result = ops[op](a, b)
    if result is None:
        return None, '0으로 나눌 수 없습니다'
    return result, None


def main():
    print('=== 계산기 ===')
    print('사용법: 숫자 연산자(+, -, *, /, **, %) 숫자  (예: 10 + 5, 2 ** 8)')
    print('종료: q 또는 quit\n')

    while True:
        expr = input('>>> ').strip()
        if expr.lower() in ('q', 'quit', 'exit'):
            print('종료합니다.')
            break
        if not expr:
            continue

        parts = expr.split()
        if len(parts) != 3:
            print('형식 오류: "숫자 연산자 숫자" 형태로 입력하세요\n')
            continue

        try:
            a = float(parts[0])
            b = float(parts[2])
        except ValueError:
            print('숫자를 올바르게 입력하세요\n')
            continue

        result, err = calculate(a, parts[1], b)
        if err:
            print(f'오류: {err}\n')
        else:
            if result == int(result):
                result = int(result)
            print(f'= {result}\n')


if __name__ == '__main__':
    main()
