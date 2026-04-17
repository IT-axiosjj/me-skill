# versioning

当生成或更新 `self.md`、`persona.md`、`profile.md` 前，先判断是否存在旧版本。

## 版本规则
- 若旧文件存在，则复制到 `versions/` 目录
- 文件名使用：`YYYYMMDD_HHMMSS_<name>.md`
- 仅在内容实际变化时创建新版本

## 适用文件
- `self.md`
- `persona.md`
- `profile.md`

## 原则
- 版本备份优先于覆盖
- 没变化就不制造新版本
