# -*- coding: utf-8 -*- #
import pythoncom
import pyHook
def onKeyboardEvent(event):
    print event.WindowName
    return True

def main():
    # 创建一个“钩子”管理对象  
    hm = pyHook.HookManager()
    # 监听所有键盘事件  
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”  
    hm.HookKeyboard()
    # hm.MouseAll = onMouseEvent
    # # 设置鼠标“钩子”  
    # hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态

    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()