# 突破10根K棒YCTSENG

日盤當沖策略：開盤後第 `Length` 根K棒建立當天高低區間，之後雙向掛突破停損單，
掛的單同時也是另一邊部位的反手/停損。

## 邏輯
- 用 `D`（日期）判斷是否為新的一天，`K` 從 1 開始逐根累加
- `K=Length` 時，記錄前 `Length` 根的高低點 `toBuy` / `toShort`
- `K>=Length` 且 `T<=endTime` 期間，同時掛買進停損單（`marketposition<=0` 時）與放空停損單
  （`marketposition>=0` 時）——這代表進場單同時也是既有部位的反手單
- `setexitonclose` + `setstoploss(25*bigpointvalue)` 做收盤平倉與保底停損

檢查下來這支邏輯是自洽的（雙邊掛單同時兼作反手/停損是常見的當沖設計），沒有發現需要修的 bug。

## 關鍵 inputs
| input | 預設 | 說明 |
|---|---|---|
| Length | 10 | 開盤區間根數 |
| endTime | 1330 | 停止新進場的時間 |

## 建議 Workspace/Chart 設定
- **商品**：日盤期貨（例如 TXF）
- **週期**：分鐘K
- **Session**：Format Symbol > Session Template 選日盤
- **口數**：於 Format Strategy > Properties 自行設定

通用匯入步驟見 `docs/SETUP.md`。
