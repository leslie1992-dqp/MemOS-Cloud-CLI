# `+add` — Add a memory

## Command

```bash
memos add -m "<text>"
```

也支持位置参数：

```bash
memos add "<text>"
```

## Common Flags

- `-m, --message` — memory text
- `--user-id`
- `--agent-id`
- `--app-id`
- `--run-id`
- `--conversation-id`
- `--json`

## Agent Example

```bash
memos add --json -m "User prefers dark mode" --user-id user_123 --conversation-id conv_456
```

## When to use

- 用户表达了稳定偏好
- 用户提供了长期有效的背景信息
- 对话中出现后续可能复用的事实

## Avoid

- 临时上下文
- 推测性的内容
- 未经许可的敏感数据
