.PHONY: help install dev-install lint test build clean publish-test

help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install package
	pip install .

dev-install: ## Install in editable mode
	pip install -e .

test: ## Run tests with pytest
	pytest tests/ -v

build: clean ## Build package
	python -m build

publish-test: build ## Upload to TestPyPI
	twine upload --repository testpypi dist/*

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
