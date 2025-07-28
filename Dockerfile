# Use a Python base image with uv
#FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
#FROM astral/uv:python3.12-alpine
FROM astral/uv:python3.12-bookworm-slim

# Set working directory
WORKDIR /app

# Enable bytecode compilation for better performance
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files (e.g., pyproject.toml, uv.lock) into the container
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself
RUN --mount=type=cache,target=/root/.cache/uv \
uv sync --locked --no-install-project
#RUN uv sync

# Copy the rest of the application code
COPY app.py .

# Install the project in non-editable mode
RUN --mount=type=cache,target=/root/.cache/uv \
uv sync --locked --no-editable

# Add the virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Command to run the application
ENTRYPOINT ["uv", "run", "python", "app.py"]
CMD ["--help"]
#CMD ["uv", "run", "python", "app.py"]
