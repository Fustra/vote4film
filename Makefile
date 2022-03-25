MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
SHELL := bash
.SHELLFLAGS := -euo pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

COLOR_BLUE = \033[0;94m
COLOR_GREEN = \033[0;32m
NO_COLOR   = \033[m


## help:	This.
.PHONY: help
help: Makefile
#	Find all double comments and treat them as docstrings
	@echo "make <command>"
	@sed -n 's/^##//p' $<


## check:	Run basic checks.
.PHONY: check
check:
	@echo -e "${COLOR_BLUE}=== Poetry ===\n${NO_COLOR}"
	@poetry --quiet check

	@echo -e "${COLOR_BLUE}\n=== Pyflakes ===\n${NO_COLOR}"
	@poetry run pyflakes src tests

	@echo -e "${COLOR_BLUE}\n=== Security: Bandit ===\n${NO_COLOR}"
	@poetry run bandit --recursive --quiet src

	@echo -e "${COLOR_BLUE}\n=== Security: Safety ===\n${NO_COLOR}"
	@poetry run safety check --bare

	@echo -e "${COLOR_BLUE}\n=== Django ===\n${NO_COLOR}"
	@poetry run ./src/manage.py check --deploy --fail-level WARNING

	@echo -e "${COLOR_BLUE}\n=== Django - missing migrations ===\n${NO_COLOR}"
	@poetry run ./src/manage.py makemigrations --dry-run --check --no-input

	@echo -e "${COLOR_BLUE}\n=== Black ===\n${NO_COLOR}"
	@poetry run black --target-version py38 --quiet --check src tests

	@echo -e "${COLOR_BLUE}\n=== isort ===\n${NO_COLOR}"
	@poetry run isort --check src tests

	@echo -e "\n${COLOR_GREEN}All Good!${NO_COLOR}"


## fix:	Fix checks where possible (black + isort).
.PHONY: fix
fix:
	@echo -e "${COLOR_BLUE}\n=== autoflake ===\n${NO_COLOR}"
	@poetry run autoflake --in-place --recursive --remove-all-unused-imports src

	@echo -e "${COLOR_BLUE}\n=== Black ===\n${NO_COLOR}"
	@poetry run black src tests

	@echo -e "${COLOR_BLUE}\n=== isort ===\n${NO_COLOR}"
	@poetry run isort src tests


## test:	Run tests.
.PHONY: test
test:
	@echo -e "${COLOR_BLUE}=== Pytest ===\n${NO_COLOR}"
	@poetry run pytest tests


##
##Run make with VERBOSE=1 for additional output.
$(VERBOSE).SILENT:
