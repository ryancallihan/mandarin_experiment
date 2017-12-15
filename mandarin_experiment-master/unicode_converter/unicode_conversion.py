#!/usr/bin/python3

import sys
import ast
import os
import glob
import pandas as pd

def read_list(input_list):
    built_list = []
    ignore_list = ['NaN', 'shift', 'left', 'right', 'up', 'down']
    for line in input_list:
        built_string = ""
        if not isinstance(line, str):
            built_list.append(built_string)
        else:
            line = ast.literal_eval(line)
            for i in line:
                if 'backspace' in i:
                    built_string = built_string[:-1]
                elif 'return' in i:
                    built_list.append(built_string)
                elif 'space' in i:
                    built_string += ' '
                elif any(substring in i for substring in ignore_list):
                    continue
                else:
                    built_string += i
    return built_list

def add_to_df(dataframe,list_to_add):
    dataframe['participant_input'] = list_to_add
    return dataframe

def save_df(dataframe, filename):
    with open(filename, "w") as file:
        dataframe.to_csv(file, sep=",")


if __name__ == "__main__":

    if len(sys.argv) > 2:
        sys.stderr.write("Usage:\npython %s PSYCHOPY_CSV_OUTPUT_PATH <-- for file\nOR\n"
                         "python %s <-- for directory\n" % (sys.argv[0], sys.argv[0]))
        sys.exit(1)

    if len(sys.argv) == 2:
        try:
            if os.path.isfile(sys.argv[1]):
                input_csv = pd.read_csv(sys.argv[1])
                save_df(add_to_df(
                    input_csv, read_list(
                        input_csv['key_resp_type.keys']
                        )
                    ),
                    filename=sys.argv[1]
                )
                print('COMPLETED CONVERSION OF', sys.argv[1])
        except:
            print("INPUT INVALID")

    else:
        try:
            for csv_file in glob.glob('*.csv'):
                input_csv = pd.read_csv(csv_file)
                save_df(add_to_df(
                    input_csv, read_list(
                        input_csv['key_resp_type.keys']
                    )
                ),
                    filename=csv_file
                )
            print('COMPLETED CONVERSION OF ALL CSV FILES IN DIRECTORY')
        except:
            print("INPUT INVALID")




