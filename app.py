from program import Program
from db import Trash
from util import Util


DB_TRASHS = []


def start_app():
    print("--------------------")
    print("1. View Trash")
    print("2. Add Trash")
    print("3. Delete Trash")
    print("4. Exit Program")
    print("--------------------")

    an = Util.custom_input()

    if an == False:
        print("[SYSTEM] 잘못 된 입력 입니다.")
        start_app()
    else:
        if an == 1:
            Program.view_trash(DB_TRASHS)
            start_app()
        elif an == 2:
            result = Program.create_trash(DB_TRASHS)

            if result is True:
                print(" [SYSTEM] 새로운 쓰레기가 추가 되었습니다.")
                start_app()
            else:
                print("[SYSTEM] 쓰레기 추가하는 실패하였습니다. 다시시도 해주세요.")
                start_app()
        elif an == 3:
            result = Program.delete_trash(DB_TRASHS)
            if result is True:
                print("[SYSTEM] 쓰레기가 삭제되었습니다.")
                start_app()
            else:
                print("[SYSTEM] 사람이 삭제에 실패했습니다. 다시시도해주세요.")
                start_app()
        elif an == 4:
            print("프로그램을 종료합니다.")
        else:
            print("[SYSTEM] 잘못 된 입렵 입니다.")
            start_app()


start_app()
