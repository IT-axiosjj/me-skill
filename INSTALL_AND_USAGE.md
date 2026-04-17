# 安装与使用指南

> 如何安装 `me-skill`，以及如何快速生成自己的第一版 me。

[返回首页](./README.md) · [作用说明](./WHAT_IS_ME_SKILL.md) · [Skill 入口](./SKILL.md)

---

## 安装

### Claude Code skill

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

### Local workflow

克隆仓库后，直接运行 Python 脚本即可。

---

## 环境要求

- Python 3
- 当前版本只使用 Python 标准库

---

## 使用

### 跑内置样例

```bash
python run_test_flow.py
```

### 只用 notes

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

### 用 notes + chat

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt
```

### 用 notes + chat + correction

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### 一次传多份材料

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

---

## 材料格式

| 类型 | 用途 |
| --- | --- |
| notes | 自述、日记摘录、偏好说明、原则与边界 |
| chat | 真实对话样本、表达方式、互动风格 |
| correction | “不像我”的表达、替代表达、显式纠正 |

### chat 示例

```text
我: 先把问题定义清楚。
朋友: 你说话挺直接，但不会压人。
```

### correction 示例

```text
不像我：太热情、太夸张、太鸡汤。
更像我：先讲清楚，再动手。
我不会这样说：直接无脑冲。
```

---

## 输出结果

生成后通常会看到：

```text
selves/<name>/
├── records.json
├── self.md
├── persona.md
├── profile.md
└── versions/
```

| 文件 | 作用 |
| --- | --- |
| `records.json` | 累计输入材料 |
| `self.md` | 你是谁 |
| `persona.md` | 你怎么说话 |
| `profile.md` | 怎么模拟你 |
| `versions/` | 更新前备份 |

---

## 注意事项

- 目前主要支持 txt / md 这类文本材料
- 暂不支持微信 / QQ 原始导出直接解析
- 分类逻辑是启发式规则，建议生成后人工修正
