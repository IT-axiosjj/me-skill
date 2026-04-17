# me-skill

> `me-skill` 的可安装镜像目录，用于放入 Claude Code skills 目录中使用。

这个目录是主仓库的 skill 镜像，目的是让 `me-skill` 以 Claude Code skill 的形式存在。

你可以把它理解成：

- 一个可安装的 skill 入口
- 一个可继续扩展的 skill 骨架
- 一个和主仓库配套的镜像目录

---

## 安装

复制本目录到以下任一位置：

```text
.claude/skills/me-skill/
```

或：

```text
~/.claude/skills/me-skill/
```

---

## 目录内容

通常建议保留：

```text
me-skill/
├── README.md
├── SKILL.md
├── create-me.md
├── list-me.md
├── update-me.md
├── prompts/
└── selves/
```

| 路径 | 作用 |
| --- | --- |
| `SKILL.md` | skill 入口说明 |
| `create-me.md` | 创建 me 的入口说明 |
| `list-me.md` | 列出 me 的入口说明 |
| `update-me.md` | 更新 me 的入口说明 |
| `prompts/` | 访谈、分析、构建、修正模板 |
| `selves/` | 示例 me 资料 |

---

## 这个目录是做什么的

这个镜像目录主要用于：

- 让 `me-skill` 作为 Claude Code skill 被安装
- 提供一个可调用的 skill 结构
- 配合主仓库中的脚本和文档一起使用

---

## 相关文档

如果你需要完整说明，请查看主仓库中的：

- `README.md`
- `INSTALL_AND_USAGE.md`
- `WHAT_IS_ME_SKILL.md`
- `SKILL.md`
