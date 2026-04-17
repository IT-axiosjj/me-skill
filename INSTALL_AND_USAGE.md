# 安装与使用指南

这份文档面向第一次接触 `me-skill` 的用户，说明如何安装、如何准备材料、以及如何快速生成自己的第一版 me。

## 1. 这是什么

`me-skill` 是一个用于整理“我是谁、我怎么说话、我的边界是什么”的个人分身工具。

它会把你的材料拆成几份结构化产物：

- `self.md`：事实、偏好、价值观、边界
- `persona.md`：表达风格、情绪态度、决策倾向、反例
- `profile.md`：最终摘要与模拟规则
- `records.json`：累计输入材料

## 2. 项目结构

核心文件：

- `SKILL.md`：skill 入口
- `tools/import_text.py`：导入纯文本材料
- `tools/import_chat.py`：导入聊天材料
- `tools/generate_me.py`：生成初版 me
- `tools/update_me.py`：用新材料更新 me
- `run_test_flow.py`：一键测试与快速生成脚本

## 3. 安装方式

### 方式一：作为普通本地项目使用

直接克隆仓库后，在项目目录运行 Python 脚本即可。

### 方式二：作为 Claude Code skill 使用

把项目内的镜像目录复制到 Claude Code 的 skills 目录：

- 项目级：`.claude/skills/me-skill/`
- 全局：`~/.claude/skills/me-skill/`

当前仓库里已经准备了镜像目录：

- `.claude/skills/me-skill/`

## 4. 环境要求

- Python 3
- 当前版本只使用 Python 标准库

## 5. 最快上手方式

在项目根目录运行：

```bash
python run_test_flow.py
```

这会使用仓库自带的测试材料，自动生成一个示例 me。

输出目录默认在：

```text
selves/generated_case/
```

## 6. 用自己的材料生成 me

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

## 7. 材料怎么准备

### notes
适合放：
- 自述
- 日记摘录
- 偏好说明
- 原则与边界

### chat
适合放：
- 你和朋友/同事的对话片段
- 你平时真实的表达方式

推荐格式：

```text
我: 先把问题定义清楚。
朋友: 你说话挺直接，但不会压人。
```

### correction
适合放：
- 不像你的表达
- 你不会说的话
- 更像你的替代表达

推荐格式：

```text
不像我：太热情、太夸张、太鸡汤。
更像我：先讲清楚，再动手。
我不会这样说：直接无脑冲。
```

## 8. 输出结果怎么看

生成后通常会看到：

- `selves/<name>/records.json`
- `selves/<name>/self.md`
- `selves/<name>/persona.md`
- `selves/<name>/profile.md`
- `selves/<name>/versions/`

其中：
- `records.json`：累计材料
- `self.md`：你是谁
- `persona.md`：你怎么说话
- `profile.md`：怎么模拟你
- `versions/`：更新前备份

## 9. 当前限制

- 还不支持微信/QQ 原始导出直接解析
- 当前更适合 txt/md 这类文本材料
- 分类逻辑是启发式规则，不是最终定稿器
- 建议生成后人工看一遍，再继续修正

## 10. 推荐使用顺序

1. 先用 notes 生成第一版
2. 再加 chat 提升风格准确度
3. 最后用 correction 明确边界和反例
4. 持续迭代 `profile.md`
