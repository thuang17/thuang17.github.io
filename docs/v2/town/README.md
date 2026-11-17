# 小镇（town）

位置：`docs/v2/town/`，不提交。镇子的页面和建造模式。

## 启动

```
cd docs/v2/tools
python3 town_server.py            # 默认端口 8180
```

- 普通模式：http://127.0.0.1:8180/
- 建造模式：http://127.0.0.1:8180/?build ，进去后按 **B** 开关。建造模式**只在本机（localhost）打开**，部署到网上后不会出现。

## 建造模式操作

| 操作 | 作用 |
|---|---|
| B | 开关建造模式 |
| 1 到 0 | 选热键栏里的物品，鼠标点地面就放下 |
| Tab 或 I | 打开背包（五个分类），点一个物品放进当前热键格 |
| H 或 Esc | 手：拖动已有物品，选中后按 Delete 删除 |
| 右键 | 删除鼠标下的物品 |
| G | 对齐网格（四分之一格）开关 |
| C | 显示碰撞范围 |
| Ctrl+Z / Ctrl+Shift+Z | 撤销、重做 |
| Shift+点击 | 把角色传送到点击位置 |
| WASD | 角色走路，镜头跟着走 |

## 保存

- 自动保存到 `docs/v2/town/layout.json`（需要 `town_server.py` 在运行）。
- 同时备份在浏览器本地；服务器没开时只存浏览器，右上角会提示。
- "Reset to default" 恢复为程序生成的默认布局，可以撤销。

## 目前能编辑什么

- 能：所有物体（建筑、树、灌木、石头、水边植物、小物件）。
- 不能：地形（草、沙路、水的形状、小径）。地形在页面代码里按规则生成。需要改地形时告诉我。
- 物体大小固定，由 `tools/sizes.json` 决定，建造模式里不能缩放。

## 留言板设计预览（2026-11-15）

- 正常打开 `http://127.0.0.1:8180/?open=Guestbook` 看留言板（不加任何参数）。
- 设计检查用：加 `&design`，会显示"DESIGN PREVIEW"横条和 0/3/30/Error 切换按钮；再加 `&notes=30` 一开始就用 30 条示例留言。这些只在 localhost 有效。
- 留言目前是示例数据（`mock-notes.json`），页面上写着"sample notes"；发送是模拟的，**什么都不会发出去**。接上真后端之后这两处提示就会去掉。
- 交给 Codex 做设计的任务书模板：`tools/codex_handoff/AGENTS.template.md`；Codex 那次的改动备份：`archive/codex_guestbook_design.patch`。
