# MultiCharts-PowerLanguage
*【FinTech】

#### 收集網路上公開的程式碼學習筆記與改進作法

為什麼想進行程式交易?

上班不能看盤

避免人性的干擾造

以上都是，但最初的夢想只是很簡單的想在金幣上衝浪和游泳而已

## 目錄結構

- `signals/<策略名稱>/strategy.pla` — 每一支交易策略（訊號）各自一個資料夾，
  搭配同資料夾內的 `README.md` 說明策略邏輯、關鍵 inputs、以及建議的 MultiCharts
  商品/週期/交易時段設定，方便一支一支獨立匯入成自己的 Workspace/Chart。
- `indicators/` — 純指標（不下單，只畫圖）。
- `docs/SETUP.md` — 在 MultiCharts 建立 Workspace/Chart、匯入策略的通用步驟。
- `docs/MC內建函數中文說明.txt` — MultiCharts 內建函數中文對照表。
