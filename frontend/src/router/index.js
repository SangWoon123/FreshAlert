import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/components/view/LoginPage.vue'
import NewProduct from '@/components/content/NewProduct.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/product',
    name: 'NewProduct',
    component: NewProduct
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
