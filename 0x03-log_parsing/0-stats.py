#!/usr/bin/python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import sys

statuscode_dict = {"200": 0, "301": 0, "400": 0, "403": 0,
                   "404": 0, "405": 0, "500": 0}
line_counter = 0
total_size = 0

try:
    for line in sys.stdin:
        line = line.strip()
        lines = line.split(" ")
        if len(lines) > 4:
            status_code = lines[-2]
            file_size = int(lines[-1])
            if status_code in statuscode_dict:
                statuscode_dict[status_code] += 1
            total_size += file_size
            line_counter += 1
            if line_counter == 10:
                line_counter = 0
                print(f'File size: {total_size}')
                for code in sorted(statuscode_dict):
                    if statuscode_dict[code] != 0:
                        print(f'{code}: {statuscode_dict[code]}')

except KeyboardInterrupt:
    pass

finally:
    print(f'File size: {total_size}')
    for code in sorted(statuscode_dict):
        if statuscode_dict[code] != 0:
            print(f'{code}: {statuscode_dict[code]}')
