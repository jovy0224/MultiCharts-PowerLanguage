# 跳空進場Bituzi

日盤跳空策略：開盤跳空超過 10 點且延續原方向、並站上/站下 120 期均線，才順勢突破進場。

## 邏輯
- `BTime`（09:05）記錄當天高低點 `THigh`/`TLow`
- `BTime`–`ETime`（09:05–12:45）之間：
  - 跳空高開 10 點以上、且突破當日高點、且高於 120 期均線 → 買進停損單
  - 跳空低開 10 點以上、且跌破當日低點、且低於 120 期均線 → 放空停損單
- 進場後固定 50 點停損，13:10 後改用近 3 根高低點追蹤停損，13:35 後市價平倉
- `setexitonclose` 保底

## 這次修復的 bug
- 原本用 `time=BTime` 精準比對抓當天高低點，若資料剛好沒有那一根K棒，`THigh`/`TLow`
  會整天停在初始值（0 / 99999），濾網形同虛設；已改用 `time>=BTime` + 旗標修正。

## 關鍵 inputs
| input | 預設 | 說明 |
|---|---|---|
| BTime | 0905 | 記錄開盤區間高低點的時間 |
| ETime | 1245 | 進場時間上限 |

## 建議 Workspace/Chart 設定
- **商品**：日盤期貨（例如 TXF）
- **週期**：分鐘K
- **Session**：Format Symbol > Session Template 選日盤
- **口數**：於 Format Strategy > Properties 自行設定

通用匯入步驟見 `docs/SETUP.md`。
