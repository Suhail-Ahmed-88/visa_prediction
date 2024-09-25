import sys

import logging

from src.logger import logging


def error_message_detail(error, error_detail: sys):
    
    _, _, exc_tb = error_detail.exc_info()  # Get the exception info
    
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name
    
    line_number = exc_tb.tb_lineno  # Get the line number
    
    error_message = f"File Name: [{file_name}]\n Line Number: [{line_number}]\n Error occurred : [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    
    def __init__(self, error_message, errror_details:sys):
        
        super().__init__(error_message)
        
        self.error_message = error_message_detail(error_message,errror_details)
        
    def __str__(self):
        
        return self.error_message


