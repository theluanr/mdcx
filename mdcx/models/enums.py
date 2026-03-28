from enum import Enum, IntEnum

# 主刮削模式:
#   Common：正常模式
#   Sort:整理模式
#   Update：更新模式
#   Read：读取模式
class MainMode(IntEnum):
    Common = 1
    Sort = 2
    Update = 3
    Read = 4
    


# 文件模式:
#   Defautl：默认
#   Single：单文件刮削
#   Agian：重新刮削
class FileMode(Enum):
    Default = 0
    Single = 1
    Again = 2