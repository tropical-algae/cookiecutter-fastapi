<!-- version list -->

## v0.1.0 (2025-11-21)

### Chores

- Optimized api url
  ([`390b00b`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/390b00b1b9f34b721a977bb5ab4abeca2ec70609))

- Optimized configuration, improve config for SQL
  ([`91d26c1`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/91d26c193527443a12247d5eabc6e777a7e2ad4f))

- Remove cov.xml from remove repo
  ([`0735611`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/0735611b5ecb640f54011b3c44e3ee9c53461282))

- Supplement test cases for new api
  ([`485d0a7`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/485d0a798e70e836e5aad04d1a5bc7a1a0769af1))

### Features

- Add a basic FastAPI with identity verification system
  ([`7226546`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/722654635b69822172d5ef88239bdc885c9bd394))

- Add basic llm agent stream inference api, add support for loading yaml configuration
  ([`7db521c`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/7db521c13eaf194a1f4ca2dd43877bb65c3fcc37))

- Add chat session for llm, optimized database basemodel and crud
  ([`057666d`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/057666d5fdeb921d18418407beed235416e05a5c))

- Add factory for agent with diff model, add new status check api and optimized session input logic
  for chat
  ([`8eb5463`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/8eb5463874feb16d498c5ac8ef12a24577242af7))

- Add support for async SQL and async function coverage checks
  ([`e6abc84`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/e6abc84673fda205118c5a4d1dbb5496300db6f3))

- Optimized chat and session api with session id as request body
  ([`5787442`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/57874428e253289993930ea765f097f90699c351))

- Replace logging with loguru, clear useless code
  ([`3008ccb`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/3008ccbe6faaa8ef087e5918603102ff74907838))

- Support dynamic agent tool selection
  ([`a8eaee1`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/a8eaee1ba45d5a05369b126e8c74ac36a3506dbf))

- Support un-stream inference, optimized called tool info response
  ([`2e95701`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/2e95701077989c19d75953af825d69ff8fb21149))

### Refactoring

- Encapsulate memory as a independent model
  ([`d17f65a`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/d17f65a054334c888de49f26f951e551bf8923a6))

### Update

- Enhance logging and resolve minor bugs
  ([`8537367`](https://github.com/tropical-algae/{{cookiecutter.project_slug}}-core/commit/85373676c4ee66a86c403362e4035ba0e9f44a8a))
