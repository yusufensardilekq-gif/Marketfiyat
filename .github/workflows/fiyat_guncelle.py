
import json
from datetime import datetime, timezone

veriler = {
    "guncelleme_zamani": datetime.now(timezone.utc).isoformat(),
    "kaynak": "Henüz market veri kaynağı bağlanmadı",
    "urunler": []
}

with open("prices.json", "w", encoding="utf-8") as dosya:
    json.dump(veriler, dosya, ensure_ascii=False, indent=2)

print("Fiyat veri dosyası hazırlandı.")
