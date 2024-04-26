import { createApp } from 'vue';
import App from './App';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import router from "@/router/router";
import components from "@/components/UI"

// import 'bootstrap-vue/dist/bootstrap-vue.css';
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';


const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app.use(router).mount('#app')
// app.use(router).use(BootstrapVue).use(IconsPlugin).mount('#app')
