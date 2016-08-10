"""####################
Author: Nathan Mador-House
Title: Py to File
####################"""

"""####################
Index:
    1. Functions
    2. Main
    3. Testing
####################"""

import json

###################################################################
# 1. FUNCTIONS
###################################################################


def text_to_file(text, filename):

    with open(filename, 'a') as text_file:
        object_type = type(text)
        if object_type is list:
            for i in text:
                text_file.write(i + '\n')
        if object_type is dict:
            print("It's a dict!")
            json.dump(text, text_file)
        else:
            text_file.write(text + '\n')


def file_to_text(filename):

    with open(filename, 'a') as from_file:
        data = json.load(from_file)
        return data


###################################################################
# 2. MAIN
###################################################################

###################################################################
# 3. TESTING
###################################################################
