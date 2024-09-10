import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/components/view/LoginPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [{ path: '/', component: LoginPage }]
})

export default router
