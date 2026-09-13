# 特定比例順勢突破當沖 by Ray's

日盤當沖策略：當天必須先出現雙向都超過 `BreakoutPct%` 的震盪，才在當日高/低點掛停損單，
順勢延續突破方向；固定百分比停損，收盤前強制平倉。

## 邏輯
- 當日高點 ≥ 開盤價×(1+BreakoutPct) 且 當日低點 ≤ 開盤價×(1-BreakoutPct) → 確認今天是雙向震盪日
- 符合條件時，在當日高點掛買進停損單、在當日低點掛放空停損單（哪邊先觸價就做哪邊）
- 固定 `StopLossPct` 百分比停損
- `FlattenTime` 之後強制平倉 + `setexitonclose` 保險

## 這次修復的 bug
- `condition1` 原本用單根K棒的開盤價（`open(0)`）而不是當日開盤價（`opend(0)`），
  跟其他三個 condition 不一致，已統一修正。

## 關鍵 inputs
| input | 預設 | 說明 |
|---|---|---|
| BreakoutPct | 0.006 | 判定雙向震盪日的門檻（0.6%） |
| StopLossPct | 0.005 | 停損百分比 |
| EntryStart | 0900 | 進場時間下限 |
| EntryEnd | 1300 | 進場時間上限 |
| FlattenTime | 1325 | 強制平倉時間 |

## 建議 Workspace/Chart 設定
- **商品**：日盤期貨（例如 TXF）
- **週期**：分鐘K，依你偏好的當沖週期
- **Session**：Format Symbol > Session Template 選日盤（0900-1325 這幾個時間才有意義）
- **口數**：於 Format Strategy > Properties 自行設定

通用匯入步驟見 `docs/SETUP.md`。
