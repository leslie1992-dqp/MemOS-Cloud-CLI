# `+delete` — Delete a memory by ID

## Command

```bash
memos delete <MEMORY_ID>
```

## Common Flags

- `--user-id`
- `--json`

## Agent Example

```bash
memos delete --json mem_123456
```

## When to use

- 用户明确要求删除某条记忆
- 已确认某条记忆过期、错误或不应保留

## Caution

- 删除前优先确认 `memory_id` 是准确的
- 如果上下文里只有模糊描述，先搜索或读取，不要直接猜测删除
