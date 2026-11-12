FROM node:24.14.1-bookworm-slim@sha256:b506e7321f176aae77317f99d67a24b272c1f09f1d10f1761f2773447d8da26c
RUN npm install --global npm@11.11.0 && test "$(node --version)" = "v24.14.1" && test "$(npm --version)" = "11.11.0"
WORKDIR /workspace
COPY package*.json ./
RUN npm ci
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev"]

