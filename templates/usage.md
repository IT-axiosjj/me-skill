# usage

## 从纯文本导入

```bash
python tools/import_text.py data/raw.txt --source self_notes --kind note --output data/self_notes.json
```

## 从简易聊天记录导入

支持：`我: xxx` 和 `我：xxx`

```bash
python tools/import_chat.py data/chat.txt --source chat_sample --output data/chat.json
```

## 用多份材料生成 me 档案

```bash
python tools/generate_me.py data/self_notes.json data/chat.json --name my_me --output-dir selves
```

## 用模板样例直接生成

```bash
python tools/generate_me.py templates/example_input.json --name demo_me --output-dir selves
```

## 增量更新已有 me

更新时会读取并累积 `selves/<slug>/records.json`，再重写 markdown 产物。

```bash
python tools/update_me.py selves/demo_me templates/example_update.json
```

## 单独备份当前版本

```bash
python tools/version_manager.py selves/demo_me
```
