# 螢幕鎖定計時器

設定倒數時間（時/分/秒），時間一到自動鎖定 Windows 螢幕。

## 使用方式

```
python screen_lock_timer.py
```

- Windows 內建 Python 即含 `tkinter`，無需安裝額外套件。
- 輸入時、分、秒後按「開始倒數」，倒數結束會呼叫 `LockWorkStation` 鎖定螢幕。
- 倒數期間可按「取消」中止。
