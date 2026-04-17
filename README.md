# me-skill

[中文](./README.md) | [English](./README_EN.md)

`me-skill` 是一个面向 **Claude Code** 的个人分身 skill，用来把你的文本材料整理成一个可持续修正、可持续迭代的 me profile。

它参考 `yourself-skill` 的方向，但当前版本更偏 **可运行的最小实现版**：

- 先收集你的 notes / chat / correction
- 再生成 `self.md`、`persona.md`、`profile.md`
- 后续可以继续追加材料、修正风格、保留版本

## 这个 skill 想解决什么问题

很多“数字分身”方案容易只停留在语气模仿，结果往往：

- 说话像，但不稳定
- 能模仿一点风格，但抓不住边界
- 不知道什么像你，也不知道什么明显不像你

`me-skill` 的目标是把这些内容拆开：

- **self**：你是谁，你的偏好、价值观、边界是什么
- **persona**：你怎么说话，你的情绪和决策倾向是什么
- **profile**：最终用于模拟和调用的摘要规则

## 适合谁用

- 想做自己的 Claude Code 分身 skill
- 想沉淀长期表达风格的人
- 想把零散材料整理成结构化个人档案的人
- 想基于这个仓库继续扩展更完整 skill 体系的人

## 文档导航

- [安装与使用指南](./INSTALL_AND_USAGE.md)
- [me-skill 是做什么的](./WHAT_IS_ME_SKILL.md)
- [Skill 入口说明](./SKILL.md)

## 在 Claude Code 里它是什么

这个仓库不是单纯的 Python 脚本集合，它的目标是作为一个 **Claude Code skill 项目** 使用。

当前仓库内已经包含：

- `SKILL.md`：skill 入口说明
- `.claude/skills/me-skill/`：可安装镜像目录
- `prompts/`：访谈、分析、构建、合并、修正模板
- `tools/`：用于跑通本地生成流程的辅助脚本

也就是说：

- 从 **GitHub 展示** 看，它是一个 skill 项目
- 从 **本地运行** 看，它又是一个能实际生成 me profile 的工作流仓库

## 当前能力

- 导入纯文本材料：`tools/import_text.py`
- 导入简易聊天材料：`tools/import_chat.py`
- 从一份或多份 records 生成 me：`tools/generate_me.py`
- 用新增材料更新已有 me：`tools/update_me.py`
- 自动保留旧版本：`tools/version_manager.py`
- 一键跑通内置样例或真实材料：`run_test_flow.py`

## 快速开始

### 1. 先直接跑内置样例

```bash
python run_test_flow.py
```

### 2. 用你自己的材料生成 me

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### 3. 只有 notes 也可以先生成第一版

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

## 安装成 Claude Code skill

如果你希望把它按 skill 的方式安装，可以把仓库中的镜像目录复制到 Claude Code 的 skills 目录：

- 项目级：`.claude/skills/me-skill/`
- 全局：`~/.claude/skills/me-skill/`

仓库内已经提供镜像目录：

- `.claude/skills/me-skill/`

## 输出结果

默认会生成到：

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

其中：

- `records.json`：累计输入材料
- `self.md`：事实 / 偏好 / 价值观 / 边界
- `persona.md`：风格 / 情绪 / 决策 / 反例
- `profile.md`：最终模拟摘要
- `versions/`：历史备份

## 当前抽取逻辑

当前版本使用轻量规则把材料拆成：

- 明确事实
- 稳定偏好
- 风格线索
- 价值观
- 边界
- 情绪与态度
- 决策倾向
- 反例 / 不像我的表达
- 代表性原句

它现在更像一个 **可运行的 MVP skill 仓库**，而不是最终形态的强智能 persona 系统。

## 当前限制

- 还不支持直接解析微信 / QQ 原始导出
- 当前更适合 txt / md 这类文本材料
- 分类逻辑主要是启发式规则，不是深度模型归纳
- 生成结果建议人工继续修正

## 一个典型工作流

1. 准备 notes
2. 再补 chat
3. 再补 correction
4. 生成第一版 me
5. 持续追加材料，逐步修正 `profile.md`

## 仓库定位

如果放在 GitHub 上，这个仓库更适合被理解成：

- 一个 Claude Code skill 项目
- 一个个人数字分身整理工具
- 一个从文本材料生成 me profile 的工作流模板
- 一个可继续扩展成完整 skill 产品的基础仓库
