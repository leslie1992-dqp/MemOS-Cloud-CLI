# `+search` — Search memories

## Command

```bash
memos search -q "<query>"
```

也支持位置参数：

```bash
memos search "<query>"
```

## Common Flags

- `-q, --query`
- `-n, --limit`
- `--user-id`
- `--agent-id`
- `--app-id`
- `--run-id`
- `--conversation-id`
- `--json`

## Agent Example

```bash
memos search --json -q "restaurants food preferences" --user-id user_123 --conversation-id conv_456
```

## Query guidance

- 使用关键词，不要把整段长对话原样塞进去
- 优先包含用户偏好、实体、主题词
- 同时有用户身份和会话身份时，尽量都传
