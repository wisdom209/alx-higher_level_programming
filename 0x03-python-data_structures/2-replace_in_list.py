#!/usr/bin/python3
if __name__ == '__main__':
    def replace_in_list(my_list, idx, element):
        if (idx >= len(my_list) or idx < 0):
            return my_list
        my_list[idx] = element
        return my_list
