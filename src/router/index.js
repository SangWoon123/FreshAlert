import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/components/view/LoginPage.vue'
import ProductList from '@/components/view/ProductList.vue'
import DiaryProductAdd from '@/components/modal/DiaryProductAdd.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: LoginPage },
    { path: '/product', component: ProductList },
    { path: '/test', component: DiaryProductAdd },
  ]
})

export default router
