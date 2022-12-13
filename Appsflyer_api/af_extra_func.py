import inspect
import ast
import numpy as np


def retrieve_name(var):
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]


def array_parsing(key, df):
    value_list = []
    for i in range(len(df)):
        if 'null' in df.iloc[i, 5]:
            df.iloc[i, 5] = df.iloc[i, 5].replace('null', 'None')
        else:
            pass
        element = ast.literal_eval(str(df.iloc[i, 5]))
        if key in element:
            element = element.get(key)
            value_list.append(element)
        else:
            value_list.append(np.NaN)
    return value_list
