# assets 文件夹结构（2026-11-14）

按类别分文件夹，新类别出现就新建，不要把东西散放在根目录。本文件夹被 `.git/info/exclude` 本地忽略，不会提交。

- `raw/`  ChatGPT 生成的原图，原样保存，不改
  - `buildings/` 建筑
  - `characters/` 主角（`_superseded/` 放被取代的旧版）
  - `ground/` 地面格子表（草、路、水、沙岸、转角等）
  - `nature/` 树、灌木、石头、花、水边植物
  - `props/` 井、长椅、路灯、围栏、告示牌等
  - `animals_fx/` 蝴蝶、小鸟、鱼、鸭子等
  - `ui/` 提示框、图标
  - `_rejected/` 否掉的图，留作对比，不使用
- `processed/` 我处理后的成品（抠图、切图、对齐），与 raw 同样分类
  - `previews/` 拼合预览图，只用来看，不是素材
- 对应关系：`raw/<类别>/` 的原图，处理结果在 `processed/<类别>/`。
- 素材清单与风格规则见上一级 `ASSET_LIST_v1.md`、`ASSET_BRIEF_v1.md`。
