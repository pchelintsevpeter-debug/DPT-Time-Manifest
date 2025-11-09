"""
dpt_core.py
Базовый модуль для работы с Digital Planetary Time (DPT)
Версия 0.1
"""

from datetime import datetime, timezone

class DPTTime:
    def __init__(self, manifest: dict):
        """
        Инициализация DPT с манифестом.
        manifest = {
            "DPT_year": 5786,
            "epoch_start": "2025-03-20T09:01:00Z",
            "epoch_end": "2026-03-20T14:46:00Z",
            "day_count": 360,
            "day_seconds": 87657.5
        }
        """
        self.DPT_year = manifest["DPT_year"]
        self.epoch_start = datetime.fromisoformat(manifest["epoch_start"].replace("Z", "+00:00"))
        self.epoch_end = datetime.fromisoformat(manifest["epoch_end"].replace("Z", "+00:00"))
        self.day_count = manifest["day_count"]
        self.day_seconds = manifest["day_seconds"]

    def utc_to_dpt(self, utc_dt: datetime) -> dict:
        """
        Конвертация UTC -> DPT
        Возвращает словарь:
        {
            "DPT_year": int,
            "day": int,
            "pt_second": float  # секунда внутри цифрового дня
        }
        """
        if utc_dt.tzinfo is None:
            utc_dt = utc_dt.replace(tzinfo=timezone.utc)
        elapsed_seconds = (utc_dt - self.epoch_start).total_seconds()
        if elapsed_seconds < 0:
            raise ValueError("UTC время до начала DPT года")
        day_index = int(elapsed_seconds // self.day_seconds) + 1
        pt_second = elapsed_seconds % self.day_seconds
        if day_index > self.day_count:
            raise ValueError("UTC время за пределами DPT года")
        return {
            "DPT_year": self.DPT_year,
            "day": day_index,
            "pt_second": pt_second
        }

    def dpt_to_utc(self, day: int, pt_second: float) -> datetime:
        """
        Конвертация DPT -> UTC
        """
        if day < 1 or day > self.day_count:
            raise ValueError("Неверный день DPT")
        if pt_second < 0 or pt_second >= self.day_seconds:
            raise ValueError("pt_second вне диапазона")
        total_seconds = (day - 1) * self.day_seconds + pt_second
        return self.epoch_start + timedelta(seconds=total_seconds)

# Пример использования
if __name__ == "__main__":
    # Минимальный пример манифеста
    manifest_example = {
        "DPT_year": 5786,
        "epoch_start": "2025-03-20T09:01:00Z",
        "epoch_end": "2026-03-20T14:46:00Z",
        "day_count": 360,
        "day_seconds": 87657.5
    }

    dpt = DPTTime(manifest_example)

    now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
    dpt_now = dpt.utc_to_dpt(now_utc)
    print(f"UTC: {now_utc} → DPT: {dpt_now}")
