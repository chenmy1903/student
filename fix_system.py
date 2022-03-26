"""恢复被电子教室迫害的系统组件
1. 任务管理器
2. 命令提示符
"""
# Copyright 2022 chenmy1903
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import ctypes

def fix_system():
    """恢复禁用的组件"""
    commands = [
        'reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system" /f',
    ]
    for c in commands:
        os.system(c)

def is_in_exe_file():
    """获取是否在exe中运行"""
    if sys.exec_prefix != os.path.dirname(sys.executable):
        return True
    return False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    print("系统功能恢复实用工具")
    fix_system()
    os.system("pause")

if __name__ == "__main__":
    if is_in_exe_file() or is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

