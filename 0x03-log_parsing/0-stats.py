#!/usr/bin/python3
import sys
import re
import signal


def signal_handler(sig, frame):
    """_summary_

    Args:
        sig (_type_): _description_
        frame (_type_): _description_
    """
    print(f'File size: {total_size}')
    for code, count in count_status_code.items():
        print(f'{code}: {count}')
        print(f'File size: {total_size}')
    sys.exit(0)


possible_statuscode = [200, 301, 400, 403, 404, 405, 500]
signal.signal(signal.SIGINT, signal_handler)
linepattern = re.compile(
    r'^\S+ - \[\d{4}-\d{2}-\d{2}\] "GET \/projects\/\d+ HTTP\/1\.1" (\d{3}) (\d+)$'
    )
line_counter = 0
total_size = 0
count_status_code = {code: 0 for code in possible_statuscode}
while(True):
    line = sys.stdin.readline().strip()
    
    if linepattern.match(line):
        file_size = linepattern.search(line).group(2)
        status_code = int(linepattern.search(line).group(1))
        total_size = total_size + int(file_size)
        count_status_code[status_code] += 1
        line_counter += 1
        print('line inputed')
        if line_counter == 3 :
            for code, count in count_status_code.items():
                print(f'{code}: {count}')
            print(f'File size: {total_size}')
    else:
        continue
