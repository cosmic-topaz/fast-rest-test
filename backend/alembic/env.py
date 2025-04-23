# backend/alembic/env.py

import sys
import os

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 🧠 경로 설정
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# 앱에서 설정 불러오기
from app.config import settings
from app.models.base import Base
from app.models import user, board

# Alembic Config 객체
config = context.config

# SQLAlchemy URL 주입
config.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)

# 로깅 설정
fileConfig(config.config_file_name)

# Metadata 설정
target_metadata = Base.metadata

def run_migrations_offline():
    context.configure(
        url=settings.SQLALCHEMY_DATABASE_URI,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()