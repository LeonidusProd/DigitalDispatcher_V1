import LoginPage from "@/pages/LoginPage.vue";
import {createRouter, createWebHistory} from "vue-router";
import RequestsManage from "@/pages/RequestsManage.vue";


const routes = [
    {
        path: '/',
        component: LoginPage
    },
    {
        path: '/requests',
        component: RequestsManage
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;