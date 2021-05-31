import module as mo



while True:
    a = input("---------------------------------------\n"
              "csv만 출력 1, png만 출력 2, csv와 png 출력 3\n"
              "---------------------------------------\n"
              "csv만 삭제 4, png만 삭제 5, csv와 png 삭제 6\n"
              "---------------------------------------\n"
              "나가기 7\n"
              "---------------------------------------\n"
              "명령어 입력창 : ")


    if a =="1":
        mo.clear_csv()
        print()
        print('csv를 출력하는 중입니다.')
        mo.make_csv()
        print()
        print('csv 출력이 완료되었습니다.')
        print()

    elif a=="2":
        mo.clear_png()
        print()
        print('png를 출력하는 중입니다.')
        mo.make_png()
        print()
        print('png 출력을 완료하였습니다.')
        print()

    elif a =="3":
        mo.clear_csv()
        mo.clear_png()
        print()
        print('csv와 png를 출력하는 중입니다.')
        mo.make_png()
        mo.make_csv() #png 다음 csv 순서 중요!!
        print()
        print('csv와 png 출력을 완료하였습니다.')
        print()

    elif a=="4":
        mo.clear_csv()
        print()
        print('csv를 삭제했습니다.')
        print()

    elif a=="5":
        mo.clear_png()
        print()
        print('png를 삭제했습니다.')
        print()

    elif a=="6":
        mo.clear_csv()
        mo.clear_png()
        print()
        print('csv와 png를 삭제했습니다.')
        print()

    elif a=="7":
        print()
        print('프로젝트를 종료합니다.')
        break
    else:
        print()
        print("명령어를 다시 입력하세요")
        print()

