# me-skill

这是 `me-skill` 的可安装镜像目录，用于放到 **Claude Code skills** 目录中使用。

## 这是什么

`me-skill` 是一个个人分身 skill，用于把用户提供的材料整理成结构化的 me profile。

它的目标不是只模仿语气，而是把以下内容分层整理：

- `self.md`：事实、偏好、价值观、边界
- `persona.md`：表达风格、情绪态度、决策倾向、反例
- `profile.md`：最终摘要与模拟规则

## 安装位置

把本目录复制到以下任一位置即可：

- 项目级：`.claude/skills/me-skill/`
- 全局：`~/.claude/skills/me-skill/`

## 目录内容

通常建议同时保留：

- `SKILL.md`
- `prompts/`
- `selves/`

其中：

- `SKILL.md`：skill 入口说明
- `prompts/`：访谈、分析、构建、修正模板
- `selves/`：已有的示例 me 资料

## 当前定位

这个镜像目录主要用于：

- 让 `me-skill` 以 Claude Code skill 的形式存在
- 提供一个可继续扩展的 skill 骨架
- 配合仓库中的工具脚本一起使用

如果你需要完整的仓库说明，请返回主仓库查看：

- `README.md`
- `INSTALL_AND_USAGE.md`
- `WHAT_IS_ME_SKILL.md`
