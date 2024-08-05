#!/bin/sh
alembic upgrade head
fastapi ./src/main.py