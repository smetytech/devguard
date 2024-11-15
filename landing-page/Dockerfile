# Build with:   docker build -t IMAGE_NAME .
# Run with:     docker run -p 3000:3000 --rm --name IMAGE_NAME IMAGE_NAME

FROM node:20.9-alpine AS builder
WORKDIR /staging
COPY . /staging/

RUN corepack enable && \
  pnpm install && \
  pnpm build && \
  pnpm prune --prod

FROM node:20.9-alpine
WORKDIR /app
COPY --from=builder /staging/package.json /staging/pnpm-lock.yaml  /app/
COPY --from=builder /staging/node_modules /app/node_modules
COPY --from=builder /staging/build /app/build

EXPOSE 3333
ENV PORT=3333
CMD ["node", "/app/build/index.js"]
#CMD ["sh", "-c", "echo $PUBLIC_API_URL && echo $PUBLIC_AUTH_API_URL && node /app/build/index.js"]

