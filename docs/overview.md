# Docs — TG media downloader
Queue and workers.
## Sequence
```mermaid
sequenceDiagram
  participant User
  participant Bot
  participant Worker
  participant Cache
  User->>Bot: link
  Bot->>Worker: enqueue
  Worker->>Cache: check
  Worker->>User: deliver
```
