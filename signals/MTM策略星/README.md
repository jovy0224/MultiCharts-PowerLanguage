# MTM策略星

動量指標(MTM)交叉搭配 RSI 濾網進場，多空各自用近期高低點的移動停損出場。

## 邏輯
- `MTM` 向上穿越其移動平均，且 `RSI(close,16)>=xx` → 做多
- `MTM` 向下穿越其移動平均，且 `RSI(close,16)<=yy` → 放空
- 多單：停損價 = 進場後創新高才更新的 `low`−`stoppoint`
- 空單：停損價 = 進場後創新低才更新的 `high`+`stoppoint1`

## 關鍵 inputs
| input | 預設 | 說明 |
|---|---|---|
| n | 9 | MTM 計算天期 |
| m | 5 | MTM 平滑天期 |
| xx | 70 | 做多的 RSI 門檻 |
| yy | 26 | 做空的 RSI 門檻 |
| stoppoint | 10 | 多單移動停損的點數緩衝 |
| stoppoint1 | 10 | 空單移動停損的點數緩衝 |

## 建議 Workspace/Chart 設定
- **商品**：不限，適合有明顯動能行情的商品
- **週期**：中長線波段，可能跨日持倉
- **Session**：不需限制交易時段
- **口數**：於 Format Strategy > Properties 自行設定

通用匯入步驟見 `docs/SETUP.md`。
