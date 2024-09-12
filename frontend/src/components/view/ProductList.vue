<template>
  <div class="product">
    <div class="header">
      <h2>재고파악</h2>
      <v-btn color="red" @click="deleteProduct">삭제</v-btn>
    </div>
    <div class="search">
      <v-text-field density="compact" variant="outlined"> </v-text-field>
      <v-btn color="green">검색</v-btn>
    </div>
    <div class="nav">
      <span>제품명</span>
      <span>유통기한</span>
      <span>개수</span>
      <span>꺼냄여부 ✅</span>
    </div>
    <v-divider thickness="3px"></v-divider>
    <div class="list">
      <div v-for="(item, index) in productStore.productList" :key="index" class="list-item">
        <span :style="style(index)">{{ item.name }}</span>
        <span :style="style(index)">{{ item.expiration }}</span>
        <span :style="style(index)">{{ item.quantity }}</span>
        <input type="checkbox" v-model="item.checked" />
      </div>
    </div>

    <div class="footer">
      <v-btn color="green" variant="outlined" @click="openDiaryModal">유통기한 등록</v-btn>
      <v-btn color="green" @click="openProductModal">제품명 등록</v-btn>
      <v-btn color="red" @click="openDeleteModal">제품명 삭제</v-btn>
    </div>

    <!-- 팝업배경흐리게 -->
    <div v-if="productModal.isOpen.value" class="backdrop">
      <div class="add-dialog" @click.stop>
        <ProductNameAdd @close="closeProductModal" />
      </div>
    </div>

    <div v-if="diaryModal.isOpen.value" class="backdrop">
      <div class="add-dialog" @click.stop>
        <DiaryProductAdd @close="closeDiaryModal" />
      </div>
    </div>

    <div v-if="deleteModal.isOpen.value" class="backdrop">
      <div class="add-dialog">
        <DiaryProductDelete @close="closeDeleteModal" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductNameAdd from '../modal/ProductNameAdd.vue'
import DiaryProductAdd from '../modal/DiaryProductAdd.vue'
import DiaryProductDelete from '../modal/DiaryProductDelete.vue'
import { useModal } from '@/util/useModal'
import { authInstance } from '@/api/authApi'
import { useProductList } from '@/stores/product'
import { onMounted } from 'vue'
import { watch } from 'vue'

//모달 상태
const productModal = useModal()
const diaryModal = useModal()
const deleteModal = useModal()
// 상태관리
const productStore = useProductList()

// 모달제어함수
const openProductModal = () => productModal.open()
const closeProductModal = () => productModal.close()

const openDiaryModal = () => diaryModal.open()
const closeDiaryModal = () => diaryModal.close()

const openDeleteModal = () => deleteModal.open()
const closeDeleteModal = () => deleteModal.close()

const products = ref([])
onMounted(async () => {
  const response = await authInstance('/products').get('')
  productStore.productList = response.data
})

const style = (index) => {
  return {
    textDecoration: productStore.productList[index].checked ? 'line-through' : 'none'
  }
}

async function deleteProduct() {
  // const deleteList = productStore.productList.filter((item) => item.checked === true)
  // const response = await authInstance('/product').delete('', { deleteList })
  console.log('제품 삭제')
}

watch(
  products,
  (newItems) => {
    newItems.forEach((item) => {
      if (item.checked && !item.delete_date) {
        item.delete_date = new Date().toISOString()
      }
    })
  },
  { deep: true }
)
</script>

<style lang="scss" scoped>
.product {
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  position: relative;
  .header {
    display: flex;
    justify-content: space-between;
  }
  h2 {
    margin-bottom: 20px;
  }
  .search {
    display: flex;
    gap: 10px;
  }

  .nav {
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding-bottom: 10px;
    :nth-child(1) {
      display: flex;
      justify-content: center;
      flex: 2;
    }
    :nth-child(2) {
      display: flex;
      justify-content: center;
      flex: 4;
    }
    :nth-child(3) {
      display: flex;
      flex: 1;
    }
  }

  .list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow-y: auto;
    max-height: 90%;
    :nth-child(1) {
      display: flex;
      justify-content: center;
      flex: 2;
    }
    :nth-child(2) {
      display: flex;
      justify-content: center;
      flex: 4;
    }
    :nth-child(3) {
      display: flex;
      flex: 1;
    }
    :nth-child(4) {
      display: flex;
      flex: 1;
    }
    .list-item {
      font-size: 12px;
      display: flex;
      gap: 10px;
      padding: 10px;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #ddd;
      color: black;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
  }

  .footer {
    width: 100%;
    height: 70px;
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 2;
    border-top: 1px solid #ddd;
    background-color: #ffffff;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.5); /* 뒷배경 흐리게 */
    z-index: 1;
  }
  .add-dialog {
    padding: 10px;
    z-index: 2;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
</style>
