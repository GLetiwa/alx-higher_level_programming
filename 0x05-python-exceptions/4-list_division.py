#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            a = my_list_1[i]
            b = my_list_2[i]

            if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
                raise TypeError("wrong type")
            if b == 0:
                raise ZeroDivisionError("division by 0")
            result1 = a / b
            result.append(result1)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
