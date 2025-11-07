import sys
import traceback

try:
    10/0
except Exception as e:
    print('error occured')
    print(e)