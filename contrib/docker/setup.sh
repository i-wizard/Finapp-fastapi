#!/bin/bash

#alembic upgrade head # Run migrations
echo Starting uvicorn ...
uvicorn main:app --host 0.0.0.0 --port 8000 --reload # Start uvicorn server