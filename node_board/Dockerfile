# 베이스 이미지 설정 (Node.js LTS 버전 사용)
FROM node:16

# 작업 디렉토리 설정
WORKDIR /app

# package.json과 package-lock.json 파일을 작업 디렉토리로 복사
COPY package*.json ./

# 프로젝트의 의존성 설치
RUN npm install

# 애플리케이션 소스 코드 복사
COPY . .

# 애플리케이션이 3000번 포트를 사용하도록 설정
EXPOSE 3000

# 애플리케이션 시작 명령어
CMD ["node", "server.js"]
