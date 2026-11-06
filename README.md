# DevAtlas AI

AI-powered engineering knowledge workspace.

**Milestone 1 foundation**
- Django REST Framework API
- React + TypeScript + Vite frontend
- PostgreSQL using the pgvector-ready image
- Redis service for future background jobs
- JWT registration and login
- Protected project workspace CRUD
- Docker Compose development environment

## Quick start

Requirements: Docker Desktop and Git.

1. Clone the repository:
   `git clone https://github.com/awaisiftikharr/DevAtlas-AI.git`
2. Enter the project:
   `cd DevAtlas-AI`
3. Copy the environment template:
   - Windows PowerShell: `Copy-Item .env.example .env`
   - macOS/Linux: `cp .env.example .env`
4. Start the stack:
   `docker compose up --build`
5. Open:
   - Frontend: http://localhost:5173
   - API health: http://localhost:8000/api/health/

Register an account in the frontend, then create your first project workspace.

## Architecture

```text
React + TypeScript (Vite)
        |
        | REST / JWT
        v
Django + Django REST Framework
        |
        +---- PostgreSQL (pgvector-ready)
        |
        +---- Redis (background task foundation)
```

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health/` | Health check |
| POST | `/api/auth/register/` | Register account |
| POST | `/api/auth/token/` | Obtain JWT tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| GET | `/api/me/` | Current user profile |
| GET/POST | `/api/projects/` | List or create own projects |
| GET/PATCH/DELETE | `/api/projects/:id/` | Manage own project |

## Roadmap

- [x] Milestone 1: authentication, project workspace, Docker foundation
- [ ] Milestone 2: document ingestion and asynchronous processing
- [ ] Milestone 3: embeddings, vector retrieval and grounded RAG answers
- [ ] Milestone 4: GitHub repository integration and source citations
- [ ] Milestone 5: answer evaluation, feedback and analytics
- [ ] Milestone 6: security hardening, tests, deployment and observability

## Development notes

The current version is a local development foundation, not production-ready. Before production deployment, add email verification, password reset, rate limiting, hardened token handling, audit logging, secure secrets management, database backups and deployment security controls.

Do not commit real credentials. Copy `.env.example` to `.env` and keep `.env` private.

## License

No license has been added yet. All rights remain with the repository owner unless a license is added.
