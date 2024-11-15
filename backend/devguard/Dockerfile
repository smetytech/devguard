FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv venv

RUN . /app/.venv/bin/activate

RUN uv pip install -r requirements.txt

CMD python main.py