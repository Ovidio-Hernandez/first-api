.PHONY: test lint run

test:
	uv run pytest -v

lint:
	uv run ruff format .
	uv run ruff check . --fix

run:
	uv run python -c "from app.main import main; main()"