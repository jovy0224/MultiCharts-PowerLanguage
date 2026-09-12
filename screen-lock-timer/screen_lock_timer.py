"""
螢幕鎖定計時器 (Screen Lock Timer)

設定倒數時間，時間一到就自動鎖定 Windows 螢幕。

使用方式:
    python screen_lock_timer.py

需求:
    - Windows 作業系統 (使用 user32.dll 的 LockWorkStation)
    - Python 3 (內建 tkinter 即可，無需額外套件)
"""

import ctypes
import sys
import tkinter as tk
from tkinter import messagebox, ttk


def lock_windows_screen() -> None:
    """呼叫 Windows API 鎖定螢幕。"""
    ctypes.windll.user32.LockWorkStation()


class ScreenLockTimerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("螢幕鎖定計時器")
        self.root.resizable(False, False)

        self.remaining_seconds = 0
        self.timer_job = None  # after() 的識別碼，用來取消倒數

        self._build_ui()

    def _build_ui(self) -> None:
        padding = {"padx": 10, "pady": 6}

        input_frame = ttk.Frame(self.root)
        input_frame.grid(row=0, column=0, **padding)

        ttk.Label(input_frame, text="時").grid(row=0, column=0)
        ttk.Label(input_frame, text="分").grid(row=0, column=1)
        ttk.Label(input_frame, text="秒").grid(row=0, column=2)

        self.hour_var = tk.StringVar(value="0")
        self.minute_var = tk.StringVar(value="10")
        self.second_var = tk.StringVar(value="0")

        vcmd = (self.root.register(self._validate_digit), "%P")

        ttk.Entry(
            input_frame, width=5, textvariable=self.hour_var,
            validate="key", validatecommand=vcmd,
        ).grid(row=1, column=0, padx=4)
        ttk.Entry(
            input_frame, width=5, textvariable=self.minute_var,
            validate="key", validatecommand=vcmd,
        ).grid(row=1, column=1, padx=4)
        ttk.Entry(
            input_frame, width=5, textvariable=self.second_var,
            validate="key", validatecommand=vcmd,
        ).grid(row=1, column=2, padx=4)

        self.countdown_label = ttk.Label(
            self.root, text="尚未開始", font=("Segoe UI", 24)
        )
        self.countdown_label.grid(row=1, column=0, **padding)

        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=2, column=0, **padding)

        self.start_button = ttk.Button(
            button_frame, text="開始倒數", command=self.start_timer
        )
        self.start_button.grid(row=0, column=0, padx=4)

        self.cancel_button = ttk.Button(
            button_frame, text="取消", command=self.cancel_timer, state="disabled"
        )
        self.cancel_button.grid(row=0, column=1, padx=4)

    @staticmethod
    def _validate_digit(new_value: str) -> bool:
        return new_value == "" or new_value.isdigit()

    def start_timer(self) -> None:
        try:
            hours = int(self.hour_var.get() or 0)
            minutes = int(self.minute_var.get() or 0)
            seconds = int(self.second_var.get() or 0)
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字。")
            return

        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds <= 0:
            messagebox.showerror("輸入錯誤", "請設定大於 0 的時間。")
            return

        self.remaining_seconds = total_seconds
        self.start_button.config(state="disabled")
        self.cancel_button.config(state="normal")
        self._tick()

    def cancel_timer(self) -> None:
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.countdown_label.config(text="已取消")
        self.start_button.config(state="normal")
        self.cancel_button.config(state="disabled")

    def _tick(self) -> None:
        hours, remainder = divmod(self.remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.countdown_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        if self.remaining_seconds <= 0:
            self.timer_job = None
            self.start_button.config(state="normal")
            self.cancel_button.config(state="disabled")
            lock_windows_screen()
            return

        self.remaining_seconds -= 1
        self.timer_job = self.root.after(1000, self._tick)


def main() -> None:
    if not sys.platform.startswith("win"):
        print("警告: 此程式使用 Windows API 鎖定螢幕，在其他作業系統上可能無法運作。")

    root = tk.Tk()
    ScreenLockTimerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
