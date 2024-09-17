import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/components/view/LoginPage.vue'
import ProductList from '@/components/view/ProductList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: LoginPage },
    { path: '/product', component: ProductList }
  ]
})

export default router
