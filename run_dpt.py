"""
Тестовый скрипт для проверки работы DPT SDK
Работает из любой папки репозитория
"""

import sys
import os

# Добавляем путь к sdk/python, чтобы Python видел dpt_core.py
sys.path.append(os.path.join(os.path.dirname(__file__), "sdk", "python"))

from dpt_core import DPTTime
import requests
from datetime import datetime, timezone

# GitHub Raw URL на JSON-манифест DPT 5786
manifest_url = "https://raw.githubusercontent.com/pchelintsevpeter-debug/DPT-Time-Manifest/main/manifests/manifest_5786.json"

# Загрузка манифеста
try:
    manifest = requests.get(manifest_url).json()
except Exception as e:
    print("Ошибка при загрузке манифеста:", e)
    exit(1)

# Инициализация DPT
dpt = DPTTime(manifest)

# Получение текущего UTC времени (timezone-aware)
now_utc = datetime.now(timezone.utc)

# Конвертация UTC -> DPT
current_dpt = dpt.utc_to_dpt(now_utc)

print("Текущее UTC:", now_utc)
print("Текущее DPT:", current_dpt)

# Пример обратной конверсии DPT -> UTC
# Передаем отдельные значения day и pt_second
reconstructed_utc = dpt.dpt_to_utc(current_dpt['day'], current_dpt['pt_second'])
print("Восстановленное UTC из DPT:", reconstructed_utc)

