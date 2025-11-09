# DPT API Reference (GitHub Raw URL)

Digital Planetary Time (DPT) — глобальная цифровая временная шкала для машин и контрактов.  
На текущем этапе сервер отсутствует, поэтому примеры используют **GitHub Raw URL** для получения JSON-манифестов и тестирования SDK.

---

## 1. Получение текущего DPT-времени

Пока нет реального API, используем Python SDK для конверсии UTC → DPT напрямую с манифеста.

```python
from dpt_core import DPTTime
import json
import requests
from datetime import datetime, timezone

# Ссылка на GitHub Raw URL манифеста
manifest_url = "https://raw.githubusercontent.com/pchelintsevpeter-debug/DPT-Time-Manifest/main/manifests/manifest_5786.json"
manifest = requests.get(manifest_url).json()

# Инициализация DPT
dpt = DPTTime(manifest)

# Получение текущего UTC-времени
now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)

# Конвертация в DPT
current_dpt = dpt.utc_to_dpt(now_utc)
print(current_dpt)

Пример вывода:

{
  "DPT_year": 5786,
  "day": 120,
  "pt_second": 452100.45
}
2. Получение JSON-манифеста DPT года

Манифест содержит все параметры года, включая Pt-единицы, длину дня и контрольные данные.

GitHub Raw URL для DPT 5786:

https://raw.githubusercontent.com/pchelintsevpeter-debug/DPT-Time-Manifest/main/manifests/manifest_5786.json


Пример содержимого:

{
  "DPT_year": 5786,
  "version": "1.0",
  "epoch_start": "2025-03-20T09:01:00Z",
  "epoch_end": "2026-03-20T14:46:00Z",
  "day_count": 360,
  "day_seconds": 87657.5,
  "pt_definition": {
    "1_pt": 0.1,
    "1_pt_second": 1.0,
    "1_pt_minute": 36.0,
    "1_pt_octave": 3600.0,
    "1_pt_hour": 36000.0,
    "1_day_pt_units": 864000.0
  },
  "checksum": "sha256-PLACEHOLDER",
  "authority": "DPT-Labs-Global-Authority",
  "signature": "base64-PLACEHOLDER",
  "comment": "Первый рабочий манифест DPT. Год от весеннего равноденствия 2025 до 2026."
}

3. Использование SDK (Python)

SDK облегчает работу с DPT и скрывает сложные расчёты.

from dpt_core import DPTTime
import json
import requests
from datetime import datetime, timezone

# Подключение манифеста с GitHub
manifest_url = "https://raw.githubusercontent.com/pchelintsevpeter-debug/DPT-Time-Manifest/main/manifests/manifest_5786.json"
manifest = requests.get(manifest_url).json()

dpt = DPTTime(manifest)

# Пример: текущее DPT-время
now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
current_dpt = dpt.utc_to_dpt(now_utc)
print(f"Current DPT: {current_dpt}")

4. Рекомендации для интеграторов

Загружайте JSON-манифесты только с доверенных источников (GitHub Raw URL).

Проверяйте checksum для контроля целостности файла.

Используйте цифровую подпись signature, когда она будет добавлена.

Всегда работайте через SDK для конверсии времени — это минимизирует ошибки.

Для новых лет создавайте новые манифесты, где пересчитывается day_seconds.

5. Примечания

На данном этапе сервер DPT отсутствует — все ссылки ведут на GitHub.

В будущем можно заменить GitHub Raw URL на реальный API

Эта схема уже позволяет тестировать и интегрировать DPT во внешние системы.
