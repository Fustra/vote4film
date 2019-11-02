COLOR_BLUE = \033[0;94m
COLOR_GREEN = \033[0;32m
NO_COLOR   = \033[m

## help:	This.
.PHONY: help
.DEFAULT: help
help: Makefile
#	Find all double comments and treat them as docstrings
	@echo "make <command>"
	@sed -n 's/^##//p' $<

## check:	Run basic checks.
.PHONY: check
check:
	@echo -e "${COLOR_BLUE}=== Poetry ===\n${NO_COLOR}"
	@poetry --quiet check

	@echo -e "${COLOR_BLUE}\n=== Django ===\n${NO_COLOR}"
	@poetry run ./src/manage.py check --deploy --fail-level WARNING

	@echo -e "${COLOR_BLUE}\n=== Django - missing migrations ===\n${NO_COLOR}"
	@poetry run ./src/manage.py makemigrations --dry-run --check

	@echo -e "${COLOR_BLUE}\n=== Security: Bandit ===\n${NO_COLOR}"
	@poetry run bandit --recursive --quiet src

	@echo -e "${COLOR_BLUE}\n=== Security: Safety ===\n${NO_COLOR}"
	@poetry run safety check --bare

	@echo -e "${COLOR_BLUE}\n=== Pyflakes ===\n${NO_COLOR}"
	@poetry run pyflakes src

	@echo -e "${COLOR_BLUE}\n=== Black ===\n${NO_COLOR}"
	@poetry run black --target-version py37 --check src

	@echo -e "${COLOR_BLUE}\n=== isort ===\n${NO_COLOR}"
	@poetry run isort --check --recursive src

	@echo -e "\n${COLOR_GREEN}All Good!${NO_COLOR}"
