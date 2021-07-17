from db import Trash


class Program:
    def view_trash(trash):
        for p in trash:
            print("-----쓰레기 목록 -----")
            print(f"종류 : {p.type}")

    def create_trash(trash):

        prev_length = len(trash)
        new_trash = Trash()
        print("--------<보기>-------")
        print("플라스틱 일반쓰레기  음식물쓰레기  캔&유리  종이 ")
        type = input("종류를 입력하세요. >>")

        new_trash.data_setter(type)
        trash.append(new_trash)

        next_length = len(trash)

        if prev_length < next_length:
            return True
        else:
            return False

    def delete_trash(trash):
        prev_length = len(trash)
        print("===============================")
        print("-----쓰레기 목록 -----")
        for t in enumerate(trash):
            print(f"{(t[0] + 1)} - {t[1].type}")
        print("===============================")

        answer = int(input("삭제할 쓰레기의 번호를 적어주세요. >>"))

        trash.pop(answer - 1)

        next_length = len(trash)

        if prev_length > next_length:
            return True
        else:
            return False
