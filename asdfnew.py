#Doing addition and division
def my_function():
  my_list = ['Multiple of 6' if i % 6 == 0 
           else 'Multiple of 2' if i % 2 == 0 
           else 'Multiple of 3' if i % 3 == 0 
           else i for i in range(1, 20)] 
  print(my_list)
  return my_list


# getting difference in previous and current comment
def compare_and_fetch_diff(file_path):
    prev_blob = ""
    prev_content = prev_blob.data_stream.read().decode("utf-8")
 
    current_blob = ""
    current_content = current_blob.data_stream.read().decode("utf-8")
 
    diff = current_content.diff(prev_blob)

import re

#extracting name of the function
def extract_comments_above_function(code, function_name):
    pattern = r"^\s*#\s*(.*)\n\s*def\s+" + function_name + r"\s*\(.*\)\s*:"    
    match = re.search(pattern, code, re.MULTILINE)     
    if match:         
        return match.group(1).strip()     
    else:         
        return None    