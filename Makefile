.PHONY: test lint run

test:
	uv run pytest -v

lint:
	uv run ruff format .
	uv run ruff check . --fix

run:
	uv run uvicorn app.main:app --reload