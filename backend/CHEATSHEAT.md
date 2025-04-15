
```bash
# 최초 마이그레이션 생성
alembic revision --autogenerate -m "initial"

# DB에 반영
alembic upgrade head
```

🐍FastAPI 백엔드 컨테이너

```bash
# 컨테이너 진입
docker exec -it fast-rest-backend-1 /bin/bash

#    -it = 터미널 연결
#   fast-rest-backend-1는 docker compose ps에서 나온 이름 그대로

# 들어간 다음
cd app

alembic revision --autogenerate -m "init"
alembic upgrade head

alembic revision --autogenerate -m "Add User and Board tables"
alembic upgrade head

```

🐬 2. MySQL 컨테이너 (DB 확인용)

```bash
# 컨테이너 진입
docker exec -it mysql-db bash

# mysql 접속
mysql -u fastapi_user -p 
# 비밀번호 입력 → supersecret

# DB 확인 
SHOW DATABASES;
USE fastapi_db;
SHOW TABLES;

```

🧠 TIP: 컨테이너 이름 까먹었을 땐

```bash
docker compose ps

# or 

# 한 줄로 자동 진입
docker exec -it $(docker ps -qf "name=backend") /bin/bash
```

Docker 초기화

```bash
# 컨테이너 실행 상태 점검
docker compose ps

# 로그 보기
docker compose logs db
```

# 초기화
docker compose down -v
docker compose up --build
```