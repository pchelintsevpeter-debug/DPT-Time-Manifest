# DPT-Time-Manifest
Digital Planetary Time - A unified planetary time, ideal for synchronizing AI, robots, autopilot, exchanges, transactions, international reports, etc.
# DPT-Time-Manifest

**Цифровой параллельный календарь (DPT) для глобальных систем и машин**

Этот репозиторий содержит:
- SDK на Python (`sdk/python/dpt_core.py`) для работы с DPT-временем  
- JSON-манифесты цифрового года (`manifests/manifest_5786.json`)  
- Тестовый скрипт `run_dpt.py` для проверки работы SDK  
- Документацию в `docs/` (спецификация, алгоритм календаря, API reference)
---
## 🔹 Быстрый старт
### 1. Клонируем репозиторий
```bash
git clone https://github.com/pchelintsevpeter-debug/DPT-Time-Manifest.git
cd DPT-Time-Manifest
Или скачать напрямую файл run_dpt.py и папку sdk/python.
2. Создаем виртуальное окружение (рекомендуется)
bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Устанавливаем зависимости
bash
pip install requests
4. Запуск тестового скрипта
bash
python run_dpt.py

Пример вывода:
Текущее UTC: 2025-11-09 02:51:45.357798+00:00
Текущее DPT: {'DPT_year': 5786, 'day': 231, 'pt_second': 34220.357798}
Восстановленное UTC из DPT: 2025-11-09 02:51:45.357798+00:00

🔹 Использование SDK в собственных проектах
python
from sdk.python.dpt_core import DPTTime
import requests
from datetime import datetime, timezone

# Загружаем манифест с GitHub
manifest_url = "https://raw.githubusercontent.com/pchelintsevpeter-debug/DPT-Time-Manifest/main/manifests/manifest_5786.json"
manifest = requests.get(manifest_url).json()

# Инициализация DPT
dpt = DPTTime(manifest)

# Пример конверсии UTC -> DPT
now_utc = datetime.now(timezone.utc)
current_dpt = dpt.utc_to_dpt(now_utc)

# Обратная конверсия DPT -> UTC
reconstructed_utc = dpt.dpt_to_utc(current_dpt['day'], current_dpt['pt_second'])

🔹 Документация
docs/specification.md — формальная спецификация DPT
docs/calendar_algorithm.md — алгоритм расчета цифрового календаря
docs/api_reference.md — инструкция по использованию SDK и манифестов

🔹 Примечания
SDK и манифесты предназначены для машинных систем и контрактов, человеческое восприятие не учитывается.
JSON-манифесты можно обновлять для новых лет без изменения SDK.
run_dpt.py доступен в репозитории для локального тестирования SDK и конверсий времени.
