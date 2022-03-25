"""提权组件
解决伽卡他卡使用SYSTEM权限运行的问题, 将破解器提到SYSTEM权限, 就能杀死伽卡他卡
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def system_upper(program: str):
    """将某个程序提权"""
    return os.system(f"{psexec} -i -d -s {program}")

def is_in_exe_file():
    """获取是否在exe中运行"""
    if sys.exec_prefix != os.path.dirname(sys.executable):
        return True
    return False

psexec = os.path.join(sys.exec_prefix, "cmd_lib", "PsExec.exe") if is_in_exe_file() else os.path.join(BASE_DIR, "cmd_lib", "PsExec.exe")

def get_pj_file():
    """获取破解器主文件"""
    if is_in_exe_file(): # 直接从exe中提取主程序
        main_file = os.path.join(sys.exec_prefix, "pj.exe")
    else: # 在py文件中运行
        main_file = os.path.join(BASE_DIR, 'pj.exe')
    return main_file # 返回地址

def main():
    system_upper(get_pj_file()) # 启动破解器

if __name__ == "__main__":
    if is_in_exe_file() or is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
