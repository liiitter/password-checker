import re

def check_password_strength(password):
    # 校验长度至少8位
    if len(password) < 8:
        return False, "密码长度至少8位"
    
    # 校验大写字母
    if not re.search(r'[A-Z]', password):
        return False, "密码必须包含至少一个大写字母"
    
    # 校验小写字母
    if not re.search(r'[a-z]', password):
        return False, "密码必须包含至少一个小写字母"
    
    # 校验数字
    if not re.search(r'[0-9]', password):
        return False, "密码必须包含至少一个数字"
    
    # 校验特殊符号（如!@#$%^&*等）
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "密码必须包含至少一个特殊符号（如!@#$%^&*）"
    
    return True, "密码强度符合要求"

if __name__ == "__main__":
    password = input("请输入密码：")
    is_strong, message = check_password_strength(password)
    print(message)