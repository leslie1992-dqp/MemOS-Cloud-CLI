---
name: memos-memory-agent
version: 1.0.0
description: "MemOS 自动记忆工作流：回答前检索、回答后写入。适合需要把记忆流程嵌入 Agent 生命周期的场景。"
metadata:
  requires:
    bins: ["memos"]
  cliHelp: "memos --help"
---

# memos-memory-agent

**CRITICAL — 开始前必须先读取：**

- [`../memos-shared/SKILL.md`](../memos-shared/SKILL.md)
- [`../memos-memory/SKILL.md`](../memos-memory/SKILL.md)

## Purpose

Automatically manage user memories during conversations.

## Rules

### Before responding

当用户提出问题或表达需求时：

1. 提炼检索关键词
2. 执行：

```bash
memos search --json -q "<query>" --user-id <USER_ID> --conversation-id <CONV_ID>
```

3. 如果命中有效记忆，将其纳入回答上下文

### After responding

当对话中出现新的稳定事实时：

1. 提炼出简洁、可复用的记忆表述
2. 执行：

```bash
memos add --json -m "<fact>" --user-id <USER_ID> --conversation-id <CONV_ID>
```

3. 仅存储长期有用的信息

## Best Practices

- 存储内容要短、准、事实化
- 搜索前优先压缩查询词
- 不要存临时任务状态
- 不要在未确认的情况下存主观推测
