# Module 06 — The Codex  

## Mastering Python’s Import System  

### Objective  

This module focuses on understanding and mastering **Python’s import mechanics** through the creation of a structured package called `alchemy`.

You will explore how Python organizes code into modules and packages, and how different import techniques affect architecture, clarity, and maintainability.

---

### What You Learn  

- Creating packages using `__init__.py`  
- Controlling what a package exposes publicly  
- Using different import styles (`import`, `from ... import`, aliasing)  
- Understanding **absolute vs relative imports**  
- Identifying and preventing circular dependencies  
- Structuring a clean, scalable Python project  

---

### Project Structure  

You progressively build a complete package:

```bash
alchemy/
│
├── __init__.py
├── elements.py
├── potions.py
│
├── transmutation/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
│
└── grimoire/
    ├── __init__.py
    ├── spellbook.py
    └── validator.py
```

With four demonstration scripts at the repository root to validate each concept.

---

### Learning Outcome  

By the end of this module, you should be able to:

- Organize Python code professionally  
- Choose the appropriate import strategy  
- Control package interfaces  
- Avoid circular import issues  
- Explain how Python resolves modules internally  

This module strengthens your ability to design clean and maintainable Python architectures.