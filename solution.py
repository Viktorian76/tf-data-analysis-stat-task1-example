import pandas as pd
import numpy as np


chat_id = 344589832 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    y = [np.log(num - 55) for num in x]
    return np.mean(y) # Ваш ответ
