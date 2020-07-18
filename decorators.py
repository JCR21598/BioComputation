#   Decorators

def section_divider(original_func):
    def wrapper(*args, **kwargs):
        print("\n\n"
              "-------------------------------------------------------------------------------------------------\n"
              "=================================================================================================\n"
              "-------------------------------------------------------------------------------------------------\n")
        return original_func(*args, **kwargs)
    return wrapper


def simple_divider(original_func):
    def wrapper(*args, **kwargs):
        print("\n\n"
              "-------------------------------------------------------------------------------------------------\n")
        return original_func(*args, **kwargs)
    return wrapper