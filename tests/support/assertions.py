def assert_dict_equals(dict_1, dict_2):
    diff_1 = dict_1.items() - dict_2.items()
    diff_2 = dict_2.items() - dict_1.items()

    msg = ""
    if len(diff_1) != 0:
        msg = f"{msg}This items {diff_1} was not be found in {dict_2}\n"
    if len(diff_2) != 0:
        msg = f"{msg}This items {diff_2} was not be found in {dict_1}\n"

    if len(msg) > 0:
        raise AssertionError(msg)
