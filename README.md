# me-skill

[中文](./README.md) | [English](./README_EN.md)

`me-skill` 是一个用于生成“个人分身档案”的 Claude Code skill / 本地工作流工具。

它的目标不是只模仿语气，而是把你的材料整理成更稳定的结构：

- 你是谁
- 你怎么说话
- 你重视什么
- 你的边界是什么
- 哪些表达明显不像你

最终产出：

- `self.md`
- `persona.md`
- `profile.md`
- `records.json`

## 适合用来做什么

- 生成自己的 AI 分身底稿
- 整理长期个人表达风格
- 把零散文本、聊天、纠正语句变成结构化资料
- 为后续更强的 persona / memory 系统打基础

## 文档导航

- [安装与使用指南](./INSTALL_AND_USAGE.md)
- [me-skill 是做什么的](./WHAT_IS_ME_SKILL.md)
- [Skill 入口说明](./SKILL.md)

## 当前能力

- 从纯文本导入材料：`tools/import_text.py`
- 从简易聊天记录导入材料：`tools/import_chat.py`
- 从一份或多份 JSON records 生成 me：`tools/generate_me.py`
- 对已有 me 做增量更新并备份旧版本：`tools/update_me.py`
- 一键跑通测试或真实材料流程：`run_test_flow.py`
- 备份当前版本：`tools/version_manager.py`

## 快速开始

### 方式一：直接跑内置样例

```bash
python run_test_flow.py
```

### 方式二：用你自己的材料

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

### 方式三：先只用 notes 生成第一版

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

## 目录结构

- `SKILL.md`：skill 入口说明
- `prompts/`：访谈、分析、构建、合并、修正模板
- `tools/`：导入、生成、更新、版本备份脚本
- `templates/`：样例输入、命令说明、使用方式
- `selves/`：生成出的个人资料

## 生成结果

默认输出到：

- `selves/<slug>/records.json`
- `selves/<slug>/self.md`
- `selves/<slug>/persona.md`
- `selves/<slug>/profile.md`
- `selves/<slug>/versions/`

## 当前抽取逻辑

生成器会用轻量规则把材料拆成：

- 明确事实
- 稳定偏好
- 风格线索
- 价值观
- 边界
- 情绪与态度
- 决策倾向
- 反例 / 不像我的表达
- 代表性原句

这不是大模型推理版分析器，而是一个可直接运行的最小实用版。

## 当前限制

- 还不支持直接解析微信/QQ 原始导出文件
- 目前主要支持纯文本和简易聊天格式
- 分类逻辑是启发式规则，适合做第一版草稿，仍建议人工修正

## 推荐用法

1. 准备自述、聊天样本、他人评价、纠正语句
2. 先导入成 JSON records
3. 用 `generate_me.py` 生成初版 me
4. 用 `update_me.py` 持续修正
5. 在 `profile.md` 中沉淀最终模拟边界

## 测试材料生成流程

下面这套流程就是仓库里已经跑通过的“自产自销”测试样例。

### 1. 准备测试材料

已生成在：

- `templates/generated_test/test_notes.txt`
- `templates/generated_test/test_chat.txt`
- `templates/generated_test/test_correction.txt`

你也可以自己新建同格式文件。

### 2. 导入测试材料

```bash
python tools/import_text.py templates/generated_test/test_notes.txt --source self_notes --kind note --output templates/generated_test/test_notes.json
python tools/import_chat.py templates/generated_test/test_chat.txt --source chat_sample --output templates/generated_test/test_chat.json
python tools/import_text.py templates/generated_test/test_correction.txt --source correction_round --kind correction --output templates/generated_test/test_correction.json
```

### 3. 生成初版 me

```bash
python tools/generate_me.py templates/generated_test/test_notes.json templates/generated_test/test_chat.json --name generated_case --output-dir selves
```

### 4. 用纠正材料更新 me

```bash
python tools/update_me.py selves/generated_case templates/generated_test/test_correction.json
```

### 5. 查看结果

结果会生成在：

- `selves/generated_case/records.json`
- `selves/generated_case/self.md`
- `selves/generated_case/persona.md`
- `selves/generated_case/profile.md`
- `selves/generated_case/versions/`

### 6. 一键运行测试流程

也可以直接在项目根目录执行：

```bash
bash run_test_flow.sh
```

或者在 Windows / Python 环境下执行：

```bash
python run_test_flow.py
```

也可以指定你自己的材料：

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt --correction path/to/correction.txt
```

如果你暂时没有纠正材料，也可以先只用 notes + chat：

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt --chat path/to/chat.txt
```

如果你连 chat 都还没有，也可以只用 notes 先生成第一版：

```bash
python run_test_flow.py --name my_me --notes path/to/notes.txt
```

如果你有多份 notes 或多份 chat，也可以一次传多个文件：

```bash
python run_test_flow.py --name my_me --notes notes_a.txt notes_b.md --chat chat_a.txt chat_b.md --correction correction.txt
```

它会自动完成：
- 导入测试材料
- 生成 `generated_case`
- 如果提供了 chat，就一并纳入生成
- 如果提供了纠正材料，就继续更新
- 打印最终输出目录和文件列表
