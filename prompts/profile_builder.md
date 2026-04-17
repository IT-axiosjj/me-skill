# profile_builder

基于 `self.md` 与 `persona.md` 生成 `profile.md`。

## 输出结构

```md
# Profile

## 一句话概述

## 这个人的核心特征
- 

## 适合如何模拟
- 

## 不应如何模拟
- 

## 回答问题时的优先级
1. 事实真实性
2. 风格一致性
3. 简洁程度
```

## 规则
- 先总结，再给规则
- profile 负责给调用者快速建立使用边界
- 不重复粘贴 self/persona 全文
