<div align="center">

# me-skill

[中文](./README.md) | [English](./README_EN.md)

![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-7C3AED)
![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![Status](https://img.shields.io/badge/Status-MVP-10B981)

**把你自己，留在数字世界里，变成一个会继续存在的 me-skill**

_记忆会散，聊天会沉，很多表达转眼就被时间带走；me-skill 想替你留住那个还在说话的“你”。_

_把偏好、语气、边界和那些“这话根本不像我”的瞬间，收进一份会慢慢生长的数字分身资料。_

[安装](#安装) · [使用](#使用) · [效果示例](#效果示例) · [文档](#文档)

</div>

---

## 安装

### 作为 Claude Code skill 安装

复制镜像目录到 Claude Code skills 目录：

```text
.claude/skills/me-skill/
```

或全局目录：

```text
~/.claude/skills/me-skill/
```

仓库内已提供镜像目录：

```text
.claude/skills/me-skill/
```

### 作为本地工具使用

克隆仓库后，直接运行 Python 脚本即可。

要求：

- Python 3
- 当前版本仅使用 Python 标准库

---

## 使用

### 最快开始

直接运行内置样例：

```bash
python run_test_flow.py
```

### 用你自己的材料生成 me

#### 只用 notes

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

#### notes + chat

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt
```

#### notes + chat + correction

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

#### 多文件输入

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

### 材料格式

#### notes

适合放：

- 自述
- 日记摘录
- 偏好说明
- 原则与边界

#### chat

推荐格式：

```text
我: 先把问题定义清楚。
朋友: 你说话挺直接，但不会压人。
```

#### correction

推荐格式：

```text
不像我：太热情、太夸张、太鸡汤。
更像我：先讲清楚，再动手。
我不会这样说：直接无脑冲。
```

### 产物说明

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
- `versions/`：更新前自动备份

---

## 效果示例

这是一个典型输出结果的结构：

```text
selves/generated_case/
├── records.json
├── self.md
├── persona.md
├── profile.md
└── versions/
```

其中：

- `self.md` 用来描述“你是谁”
- `persona.md` 用来描述“你怎么说话”
- `profile.md` 用来描述“如何模拟你”

---

## 功能特性

### 支持的输入类型

| 类型 | 用途 |
| --- | --- |
| notes | 提供自述、偏好、原则、背景信息 |
| chat | 提供真实表达方式与互动风格 |
| correction | 提供“不像我”的反例与修正 |

### 当前能力

- 导入文本材料
- 导入简易聊天记录
- 生成 me profile
- 增量更新已有 me
- 自动保留历史版本
- 支持单文件和多文件输入

### 当前抽取维度

- 明确事实
- 稳定偏好
- 风格线索
- 价值观
- 边界
- 情绪与态度
- 决策倾向
- 反例 / 不像我的表达
- 代表性原句

---

## 项目结构

```text
me-skill/
├── SKILL.md
├── prompts/
├── tools/
├── templates/
├── selves/
├── run_test_flow.py
└── .claude/skills/me-skill/
```

| 路径 | 作用 |
| --- | --- |
| `SKILL.md` | skill 入口说明 |
| `prompts/` | 访谈、分析、构建、修正模板 |
| `tools/` | 导入、生成、更新、备份脚本 |
| `templates/` | 示例材料与辅助文档 |
| `selves/` | 生成出的 me profile |
| `.claude/skills/me-skill/` | 可安装镜像目录 |

---

## 注意事项

- 目前主要支持 txt / md 这类文本材料
- 暂不支持微信 / QQ 原始导出直接解析
- 分类逻辑是启发式规则，建议生成后人工修正
- 当前版本更适合作为可运行的 MVP skill 仓库继续扩展

---

## 文档

- [安装与使用指南](./INSTALL_AND_USAGE.md)
- [me-skill 是做什么的](./WHAT_IS_ME_SKILL.md)
- [Skill 入口说明](./SKILL.md)

---

## License

MIT
