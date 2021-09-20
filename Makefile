.PHONY: clean-pyc

help:
	@echo "    shell"
	@echo "        Enters Python virtual environment"
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo "    lint"
	@echo "        Run lint script on application."
	@echo "    test"
	@echo "        Run py.test"
	@echo "    main"
	@echo "        Run main.py"

shell:
	@pipenv shell

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.pytest_cache' -exec rm -fr {} +

lint:
	@./scripts/lint

test:
	@pytest tests

main:
	@python main.py -file data/test_data.txt