# me-skill

[中文](./README.md) | [English](./README_EN.md)

一个用于构建 **个人分身资料** 的 Claude Code skill。

`me-skill` 用来把你的文本材料整理成结构化的 me profile，帮助你持续沉淀：

- 你是谁
- 你怎么说话
- 你重视什么
- 你的边界是什么
- 哪些表达不像你

## 功能

- 导入 notes、chat、correction 三类材料
- 生成 `self.md`、`persona.md`、`profile.md`
- 支持后续增量更新
- 自动保留历史版本
- 支持单文件、多文件材料输入

## 输出内容

生成结果默认位于：

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

其中：

- `self.md`：事实、偏好、价值观、边界
- `persona.md`：表达风格、情绪态度、决策倾向、反例
- `profile.md`：最终摘要与模拟规则
- `records.json`：累计输入材料

## 安装

### 作为 Claude Code skill 安装

复制镜像目录到 Claude Code skills 目录：

- 项目级：`.claude/skills/me-skill/`
- 全局：`~/.claude/skills/me-skill/`

仓库内已提供镜像目录：

- `.claude/skills/me-skill/`

### 作为本地工具使用

克隆仓库后，直接运行 Python 脚本即可。

## 快速开始

### 跑内置样例

```bash
python run_test_flow.py
```

### 用你自己的材料

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### 只用 notes 生成第一版

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

### 一次传多份材料

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

## 材料格式

### notes
适合放：
- 自述
- 日记摘录
- 偏好说明
- 原则与边界

### chat
推荐格式：

```text
我: 先把问题定义清楚。
朋友: 你说话挺直接，但不会压人。
```

### correction
推荐格式：

```text
不像我：太热情、太夸张、太鸡汤。
更像我：先讲清楚，再动手。
我不会这样说：直接无脑冲。
```

## 目录结构

- `SKILL.md`：skill 入口说明
- `prompts/`：访谈、分析、构建、合并、修正模板
- `tools/`：导入、生成、更新、备份脚本
- `templates/`：示例材料与辅助文档
- `selves/`：生成出的 me profile

## 文档

- [安装与使用指南](./INSTALL_AND_USAGE.md)
- [me-skill 是做什么的](./WHAT_IS_ME_SKILL.md)
- [Skill 入口说明](./SKILL.md)

## 当前限制

- 目前主要支持 txt / md 这类文本材料
- 暂不支持微信 / QQ 原始导出直接解析
- 分类逻辑是启发式规则，建议生成后人工修正
