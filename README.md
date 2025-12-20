# Website

Personal website built with Flask and Frozen-Flask.

**Live site:** https://jyablonski.dev

Version: 0.4.12

## Quick Start

```bash
# Install dependencies
make install

# Run development server (http://localhost:8000)
make up

# Build static site to docs/
make build
```

## Development

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Commands

| Command         | Description                             |
| --------------- | --------------------------------------- |
| `make install`  | Install dependencies                    |
| `make up`       | Run dev server at http://localhost:8000 |
| `make build`    | Build static site to `docs/`            |
| `make test`     | Run test suite                          |
| `make test-cov` | Run tests with HTML coverage report     |
| `make lint`     | Run ruff linter                         |
| `make lint-fix` | Auto-fix linting issues                 |

## Project Structure

```
.
├── .github/workflows/    # CI/CD pipelines
├── data/
│   └── projects.json     # Project data for /projects page
├── docs/                 # Built static site (generated)
├── pages/                # Markdown content pages
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── pictures/         # Images and assets
├── templates/            # Jinja2 HTML templates
├── tests/                # Test suite
├── server.py             # Flask application
├── pyproject.toml        # Project configuration
└── uv.lock               # Dependency lock file
```

## How It Works

1. **Flask** serves dynamic pages during development
2. **Flask-FlatPages** renders Markdown files from `pages/` as HTML
3. **Frozen-Flask** generates a static site to `docs/` for deployment
4. **GitHub Actions** builds and deploys to S3 on merge to `main`
