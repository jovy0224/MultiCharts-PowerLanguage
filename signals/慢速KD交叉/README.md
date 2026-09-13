# 慢速KD交叉

K/D 交叉多空反轉系統，沒有時間窗限制，可能持倉過夜。

## 邏輯
- `SlowK` 向上穿越 `SlowD` → 做多
- `SlowK` 向下穿越 `SlowD` → 放空
- 反向交叉出場；本次優化另外加了一組百分比停損（原始版本完全沒有停損）

## 關鍵 inputs
| input | 預設 | 說明 |
|---|---|---|
| Len_Short | 9 | SlowK 天期 |
| Len_Long | 10 | SlowD 天期 |
| StopLossPct | 0.02 | 相對進場價的百分比停損 |

## 建議 Workspace/Chart 設定
- **商品**：不限，適合波動、趨勢較明顯的期貨或個股
- **週期**：中長線擺盪系統，建議先用日線或較長分鐘K測試
- **Session**：不需限制交易時段（程式碼裡沒有用到 `time`）
- **口數**：於 Format Strategy > Properties 自行設定

通用匯入步驟見 `docs/SETUP.md`。
