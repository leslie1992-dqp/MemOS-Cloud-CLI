# `memos add`

Intent map:
- store a durable fact, preference, decision, or long-term task -> `memos add`
- after answering a user, pass the user's question plus the assistant's final answer into `memos add`
- do not use `--help` first when the goal is already to store a fact
- use `add` instead of `extract` or `feedback` when the user is directly asking to remember something

Use this command when:
- after answering every user question;
- when the user explicitly asks to remember, save, or store something;
- the conversation produces a memory likely to help future turns;
- you already know the memory should be stored, not just previewed.

API shape:
- `add` accepts a `messages` array, not a single plain text string;
- when called after answering, include both the user's question and the assistant's answer in that array;
- let the backend extractor decide which parts are worth persisting.

Never store:
- secrets, credentials, or tokens;
- speculative conclusions the user did not confirm;
- temporary execution state that will not matter later.

Command:

```bash
memos add "<text>"
```

Common flags:

- `-m, --message`
- `--user-id`
- `--format json`

Example:

```bash
memos add "User prefers dark mode" --user-id user_123 --format json
```

Working rules:
- `add` stores durable information only;
- do not store transient or speculative content;
- do not prepend `memos --help` when `add` is the already known goal.
