FROM python:alpine3.21

# Install bash and curl (bash needed for entrypoint.sh)
RUN apk add --no-cache bash curl
RUN apk add --no-cache postgresql-libs

# Install uv (your package manager)
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /app

# Copy pyproject.toml and lock files for caching layer
COPY pyproject.toml uv.lock* ./


# Install dependencies using uv
RUN uv pip install --system --no-cache .

# Copy app code
COPY ./app ./app

COPY alembic.ini .
COPY alembic ./alembic
COPY alembic/versions ./alembic/versions


# Expose port
EXPOSE 8000

# Run the app
CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]