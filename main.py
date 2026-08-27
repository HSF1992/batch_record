import data as dt
import service as sv

print("欢迎使用信息录入系统！")

while True:
    # 每次循环都重新读取数据（保证最新）
    数据 = dt.读取所有记录()

    choice = int(input("\n请选择项目：\n1.历史记录查询\n2.批记录查询\n3.新建记录\n4.数据统计\n5.退出程序\n"))

    if choice == 1:
        if 数据:
            for 行 in 数据:
                print(f"批号：{行[0]}，收率：{行[1]}，结果：{行[2]}")
        else:
            print("首次使用，暂无历史数据！")

    elif choice == 2:
        批号 = input("请输入查询批号：")
        结果 = sv.查找批号(批号)  # 注意：要用英文括号 ()
        if 结果:
            print(f"批号：{结果[0]}，收率：{结果[1]}，结果：{结果[2]}")
        else:
            print("无相应历史记录！")

    elif choice == 3:
        批号 = input("请输入批号：")
        收率 = float(input("请输入收率："))
        结果 = sv.判断收率是否合格(收率)  # 调用 service 里的判断函数
        dt.追加记录(批号, 收率, 结果)    # 调用 data 里的追加函数
        print(f"已录入：批号 {批号}，收率 {收率}，结果 {结果}")

    elif choice == 4:
        总批数, 合格批数, 合格率 = sv.统计合格率(数据)
        if 总批数 == 0:
            print("暂无数据，请先录入！")
        else:
            print("===== 统计结果 =====")
            print(f"总批数：{总批数}")
            print(f"合格批数：{合格批数}")
            print(f"合格率：{合格率:.1f}%")
            print("===================")

    elif choice == 5:
        print("程序已退出！")
        break

    else:
        print("无效输入，请重新选择！")
