import LoginPage from "@/pages/LoginPage.vue";
import {createRouter, createWebHistory} from "vue-router";
import RequestsManage from "@/pages/RequestsManage.vue";
import Settings from "@/pages/Settings.vue";


const routes = [
    {
        path: '/',
        component: LoginPage
    },
    {
        path: '/requests',
        component: RequestsManage
    },
    {
        path: '/settings',
        component: Settings
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;