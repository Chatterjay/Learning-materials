from date_clean import df


def output_file(file_path:str,name:str,df):
    path_name = file_path + name
    df.to_csv(path_name, index=False, encoding='utf-8-sig')