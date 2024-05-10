#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
        return div
    except (TypeError, ZeroDivisionError):
        return None
    finally:
        print("Inside result: {}".format(div))
        return div
