#!/usr/bin/python3
if __name__ == '__main__':
    def delete_at(my_list=[], idx=0):
        list_len = len(my_list)

        if (idx < 0 or idx >= list_len):
            pass
        else:
            for i in range(len(my_list)):
                if (i == idx):
                    del (my_list[i])
        return my_list
