class Util:
    def custom_input():
        answer = input(">>")

        if len(answer) > 1:
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 38 or ascii_value <= 57:
                return int(answer)
            else:
                return False
