#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import sys
import re
import signal


def signal_handler(sig, frame):
    """this is the summary"""
    print(f'File size: {total_size}')
    for code in sorted(count_status_code.keys()):
        if code in possible_statuscode:
            print(f'{code}: {count_status_code[code]}')
    sys.exit(0)


possible_statuscode = [200, 301, 400, 403, 404, 405, 500]
signal.signal(signal.SIGINT, signal_handler)
linep = re.compile(
    r'^\S+ - \[\d{4}-\d{2}-\d{2}\] '
    r'"GET \/projects\/\d+ HTTP\/1\.1" '
    r'(\d{3}) '
    r'(\d+)$'
    )
line_counter = 0
total_size = 0
count_status_code = {code: 0 for code in possible_statuscode}
try:
    for line in sys.stdin:
        line = line.strip()
        if linep.match(line):
            status_code = int(linep.search(line).group(1))
            file_size = int(linep.search(line).group(2))
            total_size = total_size + int(file_size)
            count_status_code[status_code] += 1
            line_counter += 1
            if line_counter == 10:
                print(f'File size: {total_size}')
                for code in sorted(count_status_code.keys()):
                    if code in possible_statuscode:
                        print(f'{code}: {count_status_code[code]}')
                line_counter = 0
except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)
