import random


problems_all = [
    # 近光灯
    "夜间同方向近距离跟车行驶",
    "夜间与机动车会车",
    "夜间通过有交通信号灯的路口",
    "夜间进入照明良好道路行驶",
    "前方通过路口",

    # 远近交替2次（双闪灯：向内拨动两次即可）
    "夜间通过急弯",
    "夜间通过坡道",
    "夜间通过拱桥",
    "夜间通过人行横道",
    "夜间超越前方车辆",

    # 远光灯（向外拨即可）
    "夜间进入照明不良道路行驶",

    # 关大灯，留小灯（直接转动到小灯即可，不要乱动其他）
    "在路边临时停车"
]


def init():
    problems_queue = ["下面将进行模拟夜间考试，听到语音指令后，请在5秒内做出相应的灯光操作。",
                      "请打开前照灯"
                      ]
    problems_index = random.sample(range(0, 12), 5)
    problems_index.insert(0,-1)
    problems_index.append(-2)
    for i in range(1,6):
        problems_queue.append(problems_all[problems_index[i]])
    problems_queue.append("模拟夜间考试完成，请关闭所有灯光。")
    problems_queue.append("请起步，继续完成考试。")

    return problems_index, problems_queue  # 用于生成问题
