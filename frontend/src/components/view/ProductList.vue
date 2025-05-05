<template>
  <div class="product">
    <LoadingPage v-if="isLoading" />
    <div v-else>
      <!-- 헤더 -->
      <div class="header">
        <ToggleMenu @categoryChanged="handleCategory" />
      </div>
      <!-- 컴포넌트 -->
      <component :is="currentComponent" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductAction from '../content/ProductAction.vue'
import LoadingPage from '@/components/view/Loading.vue'
import { getCategories, getProducts, getProductNames } from '@/api/authApi'
import { useProductList } from '@/stores/product'
import { onMounted } from 'vue'
import ToggleMenu from '../ToggleMenu.vue'
import CategoryAdd from '../CategoryAdd.vue'
import { useCategory } from '@/stores/category'

// 로딩
const isLoading = ref(true)
// 상태관리
const productStore = useProductList()
const categoryStore = useCategory()
// 컴포넌트
const currentComponent = ref(ProductAction)

onMounted(async () => {
  try {
    // 유통기한 리스트 가져오기
    const response = await getProducts().get()
    productStore.productList = response.data
    console.log('제품 리스트:', productStore.productList)
    console.log('제품 리스트:', response)
    // 제품명 리스트
    const productNames = await getProductNames('').get('')
    productStore.productNameList = productNames.data
    // 날짜 리스트
    productStore.updateDateList()
    // 카테고리 리스트
    const categorys = await getCategories().get()
    categoryStore.categoryList = categorys.data
  } catch (error) {
    console.error('데이터 로드 실패:', error)
  } finally {
    isLoading.value = false
  }
})

const handleCategory = (category) => {
  if (category === 'home') {
    currentComponent.value = ProductAction
  } else if (category === 'category') {
    currentComponent.value = CategoryAdd
  }
}
</script>

<style lang="scss" scoped>
.product {
  width: 100%;
  min-height: 100vh;
  background-color: #ffffff;
  position: relative;
  .header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 55px;
  }
}
</style>
