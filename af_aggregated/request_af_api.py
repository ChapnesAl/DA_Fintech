import inspect

""" получаем имена переменных """


def retrieve_name(var):
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]


media_source = [retrieve_name(x) for x in bvc]

media_source