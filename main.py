import time
import glob
import os

import camelot
import pandas as pd


def get_data_from_pdf(file_path, pages):
    return camelot.read_pdf(file_path, pages=pages, flavor='stream')

def filter_data(sort_list, table):
    sorted_df = table.df[0].isin(sort_list)
    return table.df.loc[sorted_df]

def write_to_csv(file_path, data):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    files_path_list = glob.glob(f"D:\python_apps\pdf_data_retrieve\*.pdf")
    pages = '2'
    paragraph_list = ["1.1.", "1.4.1.", "1.4.2."]
    data_dict = {"file":[], "id":[], "name": [], "code": []}

    start_time = time.time()

    for path in files_path_list:
        tables = get_data_from_pdf(file_path=path, pages=pages)
        df_data = filter_data(sort_list=paragraph_list, table=tables[0])

        data_dict['file'].append(os.path.split(path)[1].replace('.pdf', ''))
        data_dict['id'].append(df_data[2][2])
        data_dict['name'].append(df_data[2][12])
        data_dict['code'].append(df_data[2][13])

    write_to_csv(file_path='data.csv', data=data_dict)

    print(f"PDF scan in {format(time.time() - start_time, '.2f')} sec")