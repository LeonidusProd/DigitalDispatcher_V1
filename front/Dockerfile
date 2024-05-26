FROM node:14

WORKDIR /app

COPY package*.json ./
RUN #apk add --no-cache bash
RUN npm install -g @vue/cli
RUN npm install

COPY . .

RUN npm run build
#
#CMD ["npm", "run", "serve"]