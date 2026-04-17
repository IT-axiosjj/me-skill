# commands

这个文件定义 me-skill 的推荐命令式入口语义，方便你后续继续做成多个 skill 或 slash command。

## /create-me
用途：首次创建一个 me 档案

执行语义：
1. 采集基础信息
2. 收集原始材料
3. 生成 `self.md`
4. 生成 `persona.md`
5. 生成 `profile.md`

## /update-me <slug>
用途：向已有 me 追加材料

执行语义：
1. 读取 `selves/<slug>/`
2. 判断新增内容属于事实、风格还是纠正
3. 备份旧版本
4. 最小修改相关文件
5. 更新 `profile.md`

## /list-me
用途：列出当前已有 me

执行语义：
- 枚举 `selves/` 下所有子目录
- 忽略空目录与无 `profile.md` 的目录

## /show-me <slug>
用途：展示某个 me 的摘要

执行语义：
- 优先显示 `profile.md`
- 可附带 `self.md` 与 `persona.md` 路径

## /rollback-me <slug>
用途：回滚某个 me 的历史版本

执行语义：
- 列出 `versions/` 下候选版本
- 由用户确认后恢复
