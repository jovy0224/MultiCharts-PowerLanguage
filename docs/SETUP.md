# 在 MultiCharts 建立獨立 Workspace/Chart 的步驟

每一支策略都放在 `signals/<策略名稱>/strategy.pla`，底下的步驟對每一支都通用，
只有 Symbol / 週期 / Session / inputs 要照各策略資料夾裡的 README 調整。

1. **File > New > Workspace**，另存新檔，workspace 檔名建議跟策略資料夾同名（例如
   `特定比例順勢突破當沖.wsp`），方便之後對照哪個 workspace 對應哪支策略，彼此獨立、互不干擾。
2. 在新 Workspace 裡開一張新 Chart，Symbol / 週期照該策略 README 的建議設定。
3. 右鍵 Chart → **Insert Study/Strategy → PowerLanguage Editor**，開一個新的
   Signal（或 Strategy），把 `strategy.pla` 的內容整份貼進去，**Compile**。
4. 掛上策略後，打開 **Format Strategy**，依照該策略 README 列出的 inputs 表調整參數
   （百分比停損、進出場時間、天期等）。
5. 有用到 `time`/`T`/`BTime`/`EndTime` 這類時間篩選的策略，記得到
   **Format Symbol → Session Template** 選對交易所的日盤時段，程式碼裡的時間判斷才會對得上。
6. 口數/資金管理在 Format Strategy 的 **Properties for All Signals** 裡設定，程式碔本身沒有寫死口數。
7. 存檔 Workspace。之後開哪個 Workspace 就是哪支策略的獨立回測/監控環境。
