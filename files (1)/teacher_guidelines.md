# 👨‍🏫 TEACHER GUIDELINES
### FastAPI First Steps — Lecture Delivery Guide

---

## ⏱️ Timing Breakdown

| Section | Duration | Notes |
|---|---|---|
| Intro | 2 min | High energy, set the hook |
| Project Setup (UV) | 4 min | Show terminal live |
| Writing Code | 5 min | Type slowly, don't copy-paste |
| Code Walkthrough | 8 min | Slowest section — explain everything |
| Running Server | 3 min | Show in browser live |
| Interactive Docs | 4 min | Click around Swagger UI live |
| OpenAPI | 3 min | Show the JSON in browser |
| HTTP Methods | 2 min | Quick overview |
| Real World Context | 1 min | Motivation boost |
| Recap | 1 min | Tight, clear summary |
| **Total** | **~33 min** | Edit pauses to target 25 min |

---

## 🎥 Screen Recording Setup

- **VS Code** open on the left (80% of screen)
- **Terminal** at the bottom panel inside VS Code (integrated terminal)
- **Browser** for demo sections — keep tabs pre-opened:
  - `http://127.0.0.1:8000`
  - `http://127.0.0.1:8000/docs`
  - `http://127.0.0.1:8000/redoc`
  - `http://127.0.0.1:8000/openapi.json`
- Font size: **18–20pt** in both VS Code and terminal for readability
- VS Code theme: Use a high-contrast theme (e.g., One Dark Pro or GitHub Dark)

---

## ✍️ Live Coding Tips

### DO:
- **Type the code live** — don't paste. Students learn from watching you type, make typos, and correct them. It normalizes mistakes.
- **Pause after each new concept** — say "take a second to let that sink in" before moving on.
- **Narrate what you're doing** — "I'm now saving the file... you can see the server auto-reloaded in the terminal."
- **Use the browser** live when demoing — click "Try it out" in Swagger UI and actually run the request on camera.
- **Zoom in on the terminal** when showing server output.

### AVOID:
- Don't rush through the code walkthrough — Section 3 is the most important part.
- Don't assume students know what "async" means — just say "we'll cover this in detail later."
- Don't skip the OpenAPI section — it's a key FastAPI differentiator.
- Don't have a cluttered desktop visible in screen recordings.

---

## 💬 Common Student Questions & Answers

**Q: Why `async def` and not just `def`?**
A: "Both work! FastAPI supports both. `async def` allows the server to handle multiple requests simultaneously without blocking. For now, use `async def` as a habit — we'll cover the full explanation in the async lecture."

**Q: Can I use a different variable name instead of `app`?**
A: "Technically yes, but `app` is the universal convention and is what FastAPI CLI looks for by default. Stick with `app` for now."

**Q: What's the difference between `fastapi dev` and `fastapi run`?**
A: "`fastapi dev` is for development — it auto-reloads on file changes. `fastapi run` is for production — no auto-reload, optimized for performance. Never use `dev` in production."

**Q: Does FastAPI work with Python 2?**
A: "No. FastAPI requires Python 3.8 minimum, but we strongly recommend Python 3.10+ to take advantage of modern type hint syntax."

**Q: Is Uvicorn installed automatically?**
A: "Yes! FastAPI includes it as a dependency. When you run `fastapi dev`, it uses Uvicorn under the hood as the ASGI server."

**Q: What is ASGI?**
A: "ASGI stands for Asynchronous Server Gateway Interface — it's the async evolution of WSGI (used by Flask/Django). FastAPI is an ASGI framework, which is a big part of why it's so fast."

---

## ⚠️ Potential Pitfalls to Anticipate

| Problem | Cause | Fix |
|---|---|---|
| `fastapi: command not found` | Not in the UV virtual environment | Run `source .venv/bin/activate` or use `uv run fastapi dev main.py` |
| Port 8000 already in use | Another process is running | Use `fastapi dev main.py --port 8001` |
| Server doesn't auto-reload | File saved outside the watched directory | Make sure `main.py` is in the project root |
| Browser shows "Connection refused" | Server not running | Check terminal for errors |
| Docs page is empty | `app` variable named differently | Rename to `app` or configure via `--app` flag |

---

## 🎨 Emphasis Points (Highlight These)

Mark these moments in your recording — they make great chapter markers on Udemy:

1. **"6 lines of code"** — after writing main.py
2. **The decorator explanation** — `@app.get("/")` is the key concept
3. **First browser visit** — seeing `{"message": "Hello World"}` in real time
4. **Opening Swagger UI** — this always gets a reaction from new students
5. **The openapi.json reveal** — connects the dots on why auto-docs exist

---

## 🧠 Pedagogical Notes

- **Scaffolding:** Start with working code FIRST, then explain. Students stay engaged when they see results before theory.
- **Analogies used in script:** Restaurant (app instance), toolbox (import). Reinforce these with your own words.
- **Motivation:** Remind students that what Flask/Django developers spend days configuring, FastAPI gives them for free (docs, validation, serialization).
- **Preview next lecture:** Always end by teasing what's next (path parameters). This reduces drop-off.

---

## 📋 Pre-Lecture Checklist

- [ ] UV is installed on your system (`uv --version` works)
- [ ] Python 3.10+ is available (`python --version`)
- [ ] VS Code is open with a clean, empty project folder
- [ ] No other processes running on port 8000
- [ ] Browser tabs pre-opened (just not loaded yet)
- [ ] Terminal font size bumped up for visibility
- [ ] Microphone tested — no background noise
- [ ] Screen recorder running at 1080p minimum

---

*Good luck! Students love this lecture — the "wow" moment when they see Swagger UI auto-generated is one of the best first impressions in any Python course.*
