FROM node:14

WORKDIR /dd_front
COPY package*.json ./
RUN npm install

COPY . .

#RUN npm run build
#
#CMD ["npm", "run", "serve"]