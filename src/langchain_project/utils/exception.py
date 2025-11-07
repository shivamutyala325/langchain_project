import sys
import traceback

def getErrorDetails(error):
    _,_,exc_tb=sys.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error_message=f"an Error [{str(error)}] occured in python script name [{file_name}] line number [{line_no}]"
    return error_message



class CustomException(Exception):
    def __init__(self,error):
        super().__init__(error)
        self.error_message=getErrorDetails(error)

    def __str__(self):
        return self.error_message

        