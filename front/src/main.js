import { createApp } from 'vue';
import App from './App';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import router from "@/router/router";
import components from "@/components/UI"
import store from "@/store/index";

// import 'bootstrap-vue/dist/bootstrap-vue.css';
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';

const cors = require('cors');
// const corsOptions ={
//     origin:'http://localhost:8080',
//     credentials:true,            //access-control-allow-credentials:true
//     optionSuccessStatus:200
// }
const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(router)
    .use(store)
    // .use(cors())
    .mount('#app')
