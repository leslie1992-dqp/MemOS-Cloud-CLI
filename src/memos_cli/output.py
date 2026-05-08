"""Output formatting for MemOS CLI — text, JSON, table modes."""
from __future__ import annotations

import json
from datetime import datetime
from typing import Any
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def format_memories_text(console: Console, memories: list[dict], title: str = "memories") -> None:
    """Render memories in human-friendly text mode."""
    count = len(memories)
    console.print(f"\n[bold blue]Found {count} {title}:[/]\n")
    
    for i, mem in enumerate(memories, 1):
        memory_text = mem.get("memory", mem.get("text", ""))
        mem_id = mem.get("id", "")
        score = mem.get("score")
        created = _format_date(mem.get("created_at"))
        
        line = Text()
        line.append(f"{i}. ", style="bold")
        line.append(memory_text, style="white")
        console.print(line)
        
        details = []
        if score is not None:
            details.append(f"Score: {score:.2f}")
        if mem_id:
            details.append(f"ID: {mem_id}")
        if created:
            details.append(f"Created: {created}")
        
        if details:
            detail_str = " · ".join(details)
            console.print(f"     [dim]{detail_str}[/]")
        
        console.print()


def format_json(console: Console, data: Any) -> None:
    """Output data as pretty-printed JSON."""
    console.print_json(json.dumps(data, default=str))


def format_single_memory(console: Console, mem: dict, output: str = "text") -> None:
    """Format a single memory for display."""
    if output == "json":
        format_json(console, mem)
        return
    
    memory_text = mem.get("memory", mem.get("text", ""))
    mem_id = mem.get("id", "")
    
    lines = []
    lines.append(f"  [white bold]{memory_text}[/]")
    lines.append("")
    
    if mem_id:
        lines.append(f"  [dim]ID:[/] {mem_id}")
    
    created = _format_date(mem.get("created_at"))
    if created:
        lines.append(f"  [dim]Created:[/] {created}")
    
    content = "\n".join(lines)
    panel = Panel(
        content,
        title="[blue]Memory[/]",
        title_align="left",
        border_style="blue",
        padding=(1, 1),
    )
    console.print()
    console.print(panel)
    console.print()


def format_add_result(console: Console, result: dict | list, output: str = "text") -> None:
    """Format the result of an add operation."""
    if output == "json":
        format_json(console, result)
        return
    
    if output == "quiet":
        return
    
    results = result if isinstance(result, list) else result.get("results", [result])
    
    if not results:
        console.print("  [dim]No memories extracted.[/]")
        return
    
    console.print()
    
    for r in results:
        memory = r.get("memory") or r.get("text") or ""
        mem_id = r.get("id") or r.get("memory_id") or ""
        
        icon = "[green]+[/]"
        label = "Added"
        
        parts = [f"{icon}[dim]{label:<10}[/]"]
        if memory:
            parts.append(f"[white]{memory}[/]")
        if mem_id:
            parts.append(f"[dim]({mem_id})[/]")
        
        console.print("  ".join(parts))
    
    console.print()


def format_chat_result(console: Console, result: dict, output: str = "text") -> None:
    """Format chat output."""
    if output == "json":
        format_json(console, result)
        return

    answer = result.get("answer", "")
    if answer:
        console.print()
        console.print(answer)
        console.print()
        return

    console.print("  [dim]No chat response returned.[/]")


def format_agent_envelope(
    console: Console,
    *,
    command: str,
    data: Any,
    duration_ms: int | None = None,
    scope: dict | None = None,
    count: int | None = None,
):
    """Output structured JSON envelope for agent/programmatic use (--json mode)."""
    envelope: dict[str, Any] = {
        "status": "success",
        "command": command,
    }
    
    if duration_ms is not None:
        envelope["duration_ms"] = duration_ms
    
    if scope:
        filtered = {k: v for k, v in scope.items() if v}
        if filtered:
            envelope["scope"] = filtered
    
    if count is not None:
        envelope["count"] = count
    
    envelope["data"] = data
    
    console.print_json(json.dumps(envelope, default=str))


def _format_date(date_str: str | None) -> str | None:
    """Format ISO date string to readable format."""
    if not date_str:
        return None
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return date_str
