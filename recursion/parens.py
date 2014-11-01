

def parens(all_strs, left_rem, right_rem, current_str):
    # something went wrong, OH NO
    if left_rem < 0 or left_rem > right_rem:
        #ABORT
        print "something went wrong OH NO"
        return None

    if left_rem == 0 and right_rem == 0:
        # YAY WE ARE DONE
        all_strs.append(current_str)
        print all_strs
        return all_strs

    if left_rem > 0:
        new_str = current_str + "("
        parens(all_strs, left_rem - 1, right_rem, new_str)

    if right_rem > left_rem:
        new_str = current_str + ")"
        parens(all_strs, left_rem, right_rem - 1, new_str)


if __name__ == "__main__":
    arrs = parens([], 3, 3, "")
    print arrs
