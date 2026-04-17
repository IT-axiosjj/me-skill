# 安装与使用指南

这份文档面向第一次接触 `me-skill` 的用户，重点说明：

- 它如何作为 **Claude Code skill** 使用
- 它如何作为 **本地工作流工具** 跑通
- 用户应该如何准备材料并生成自己的第一版 me

## 1. 这是什么

`me-skill` 是一个用于整理“我是谁、我怎么说话、我的边界是什么”的个人分身 skill。

它会把你的材料整理成几份结构化产物：

- `self.md`：事实、偏好、价值观、边界
- `persona.md`：表达风格、情绪态度、决策倾向、反例
- `profile.md`：最终摘要与模拟规则
- `records.json`：累计输入材料

## 2. 它有两种使用方式

### 方式一：作为 Claude Code skill 使用

这是这个仓库更核心的定位。

你可以把它安装到 Claude Code 的 skills 目录中，让它以 skill 项目的方式存在。

### 方式二：作为本地工作流工具使用

当前仓库也附带 Python 脚本，方便你在本地先把材料跑通、生成和更新 me profile。

## 3. 如何安装成 skill

把仓库里的镜像目录复制到 Claude Code 的 skills 目录：

- 项目级：`.claude/skills/me-skill/`
- 全局：`~/.claude/skills/me-skill/`

当前仓库已经提供镜像目录：

- `.claude/skills/me-skill/`

安装后，你可以把这个仓库作为一个 Claude Code skill 项目来使用和继续扩展。

## 4. 如何作为本地工具使用

直接克隆仓库后，在项目目录运行 Python 脚本即可。

## 5. 环境要求

- Python 3
- 当前版本只使用 Python 标准库

## 6. 最快上手方式

在项目根目录运行：

```bash
python run_test_flow.py
```

这会使用仓库自带的测试材料，自动生成一个示例 me。

输出目录默认在：

```text
selves/generated_case/
```

## 7. 用自己的材料生成 me

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

## 8. 材料怎么准备

### notes
适合放：
- 自述
- 日记摘录
- 偏好说明
- 原则与边界

### chat
适合放：
- 你和朋友 / 同事的对话片段
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

## 9. 输出结果怎么看

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

## 10. 当前限制

- 还不支持微信 / QQ 原始导出直接解析
- 当前更适合 txt / md 这类文本材料
- 分类逻辑是启发式规则，不是最终定稿器
- 建议生成后人工看一遍，再继续修正

## 11. 推荐使用顺序

1. 先用 notes 生成第一版
2. 再加 chat 提升风格准确度
3. 最后用 correction 明确边界和反例
4. 持续迭代 `profile.md`
