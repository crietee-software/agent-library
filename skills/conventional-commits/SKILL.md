---
name: conventional-commits
description: Write git commit messages in English that follow Conventional Commits, and squash a branch into one clean commit. Use when the user asks to commit, write a commit message, squash commits, or tidy up history. Not for PR descriptions or changelog files.
---

# Conventional commits

Every commit message is English and follows Conventional Commits 1.0.

## Format

```text
<type>(<optional scope>): <summary in the imperative, lowercase, no full stop, max 72 characters>

<body: what changed and why, wrapped at 72 characters, one paragraph or a short list>

<footer: BREAKING CHANGE: ... or issue references, only when they apply>
```

## Types

| Type | Use for |
| --- | --- |
| `feat` | a new user-visible capability |
| `fix` | a bug fix |
| `docs` | documentation only |
| `refactor` | a change that neither fixes a bug nor adds a feature |
| `perf` | a change that makes something faster |
| `test` | adding or fixing tests |
| `build` | build system, package manager, dependencies |
| `ci` | CI configuration |
| `chore` | anything else that does not change code behaviour |

## Rules

1. Summary: imperative mood ("add", not "added"), no full stop, 72 characters at most.
2. Body: explain the why, not a diary of steps. Skip the body only for trivial changes.
3. One logical change per commit. Split unrelated changes.
4. Breaking changes: add `!` after the type or a `BREAKING CHANGE:` footer.
5. No model names, tool names or AI attribution in the message unless the repository asks for it.
6. Write in English even when the conversation is in another language.

## Squashing a branch into one commit

Only on commits that are not pushed yet.

1. Check what is there: `git log --oneline <base>..HEAD`.
2. Find the base commit that should stay: the last commit before your work.
3. `git reset --soft <base>` keeps all changes staged.
4. Write one message for the whole change, following the rules above.
5. Commit, then check with `git show --stat HEAD`.

Never squash or rewrite commits that are already pushed to a shared branch.

## Example

```text
feat(chat): add Claude and Grok chat over local CLIs

Run the claude and grok CLIs as subprocesses and stream their output to
the browser. Conversations keep one session per CLI, so switching models
mid-conversation passes along the messages the other model has not seen.
```
