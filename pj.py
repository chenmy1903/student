"""伽卡他卡破解器主程序
基于旧版伽卡他卡破解器
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

import psutil
import tqdm
import os

__version__ = "3.0"

def main():
    print(f"伽卡他卡破解器{__version__}")
    pids = psutil.pids()
    count = 0 # 破解器战绩
    t = tqdm.tqdm(desc="寻找受害对象", total=len(pids))
    for pid in pids:
        process = psutil.Process(pid)
        try:
            name = process.name()
        except:
            pass
        else:
            if name.lower() in ['student.exe', "studentmain.exe"]:
                path = process.exe()
                process.kill()
                # os.remove(path)
                count += 1 # 战绩+1
        t.update(1)
    if count:
        print(f"找到{count}个伽卡他卡程序, 并全部杀死")
    else:
        print("未找到任何伽卡他卡的进程")
    os.system("pause")

if __name__ == "__main__":
    main()

