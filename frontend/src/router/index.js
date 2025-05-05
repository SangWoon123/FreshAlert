import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/components/view/LoginPage.vue'
import Ato from '@/components/content/Ato.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: LoginPage },
    { path: '/product', component: () => import('@/components/content/NewProduct.vue') },
    { path: '/ato', component: Ato }
  ]
})

export default router
