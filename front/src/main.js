import { createApp } from 'vue'
import App from './App'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import router from "@/router/router"

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

const app = createApp(App)

// components.forEach(component => {
//     app.component(component.name, component)
// })

app.use(router).mount('#app')
