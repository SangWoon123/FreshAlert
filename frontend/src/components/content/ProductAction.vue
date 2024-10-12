<template>
  <div>
    <!-- 카테고리 선택 -->
    <div class="category">
      <h4>카테고리</h4>
      <CategoryTabs v-model="selectedCategory" />
    </div>

    <!-- 검색창 -->
    <div class="search">
      <v-text-field v-model="searchQuery" label="검색" density="compact" variant="outlined">
      </v-text-field>
    </div>

    <table>
      <thead>
        <tr>
          <th>제품명</th>
          <th width="80px">유통기한</th>
          <th>개수</th>
          <th width="75px">꺼냄여부 ✅</th>
        </tr>
      </thead>
      <tbody>
        <!-- 유통기한 제품리스트 -->
        <template v-for="(item, index) in filteredProductList" :key="index">
          <!-- 날짜구분선 -->
          <div class="date" v-if="item.isNewDate">
            <span>{{ item.expiration }}</span>
          </div>
          <!-- 유제품 리스트 -->
          <tr class="list">
            <td>{{ item.name }}</td>
            <td>{{ item.expiration }}</td>
            <td>{{ item.quantity }}</td>
            <td>
              <input id="check_btn" type="checkbox" :disabled="isChecked(item.expiration)" />
            </td>
          </tr>
        </template>
      </tbody>
    </table>

    <div class="footer">
      <CustomButton color="#3E8F88" icon name="유통기한" type="추가하기" @click="openDiaryModal" />
      <CustomButton color="#3E8F88" icon name="제품명" type="추가하기" @click="openProductModal" />
      <CustomButton color="#C2546E" name="제품명" type="삭제하기" @click="openDeleteModal" />
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
import { computed, ref, watch } from 'vue'
import ProductNameAdd from '../modal/ProductNameAdd.vue'
import DiaryProductAdd from '../modal/DiaryProductAdd.vue'
import DiaryProductDelete from '../modal/DiaryProductDelete.vue'
import CustomButton from '../CustomButton.vue'
import { useModal } from '@/util/useModal'
import { useProductList } from '@/stores/product'
import { useCategory } from '@/stores/category'
import CategoryTabs from './category/CategoryTabs.vue'
import { authInstance } from '@/api/authApi'

// 카테고리 선택 상태
const categoryStore = useCategory()
const selectedCategory = ref(categoryStore.selectedCategory)

// 모달 상태
const productModal = useModal()
const diaryModal = useModal()
const deleteModal = useModal()

// 모달 제어 함수
const openProductModal = () => productModal.open()
const closeProductModal = () => productModal.close()

const openDiaryModal = () => diaryModal.open()
const closeDiaryModal = () => diaryModal.close()

const openDeleteModal = () => deleteModal.open()
const closeDeleteModal = () => deleteModal.close()

// 오늘 날짜 + 1일을 계산하는 함수
const getTomorrow = () => {
  const today = new Date()
  today.setDate(today.getDate() + 1)
  return today.toISOString().split('T')[0]
}

// 제품의 만료일이 내일인 경우만 셀렉션 활성화
const isChecked = (expiration) => {
  return expiration !== getTomorrow()
}

// 검색
const searchQuery = ref('')
// 검색어 필터링 및 날짜 변화지점 확인
const productStore = useProductList()
const filteredProductList = computed(() => {
  let previousDate = null

  // 선택된 카테고리 찾기
  const selectedCategoryItem = categoryStore.categoryList[selectedCategory.value]

  // 선택된 카테고리가 '유제품'인지 확인하고 리스트 선택
  const products =
    selectedCategoryItem && selectedCategoryItem.name === '유제품'
      ? productStore.productList
      : productStore.categoryProductList

  return products
    .filter((item) => item.name.toLowerCase().includes(searchQuery.value.toLowerCase()))
    .map((item) => {
      const isNewDate = previousDate !== item.expiration
      previousDate = item.expiration
      return {
        ...item,
        isNewDate
      }
    })
})

watch(selectedCategory, async (newValue) => {
  const category = categoryStore.categoryList[newValue]
  if (category.name !== '유제품') {
    const response = await authInstance('/products/category').get(
      `/${newValue + 1}/${category.diary}`
    )
    productStore.categoryProductList = response.data
  }
})
</script>

<style lang="scss" scoped>
.search {
  display: flex;
  gap: 10px;
}

.list {
  font-size: 12px;
  color: black;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  gap: 10px;
  overflow-y: auto;
  max-height: 90%;
  .list-item {
    font-size: 12px;
    display: flex;
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
  z-index: 1;
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
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}
thead {
  border-bottom: 1px solid #ddd;
  tr {
    th {
      text-align: center;
      padding: 6px;
    }
  }
}

tbody {
  tr {
    td {
      padding: 10px;
      text-align: center;
      border-bottom: 1px solid #ddd;
    }
  }
  .date {
    display: flex;
    padding: 14px;
    font-size: 16px;
    color: #3f51b5;
  }
}
input {
  width: 14px;
  height: 14px;
}
.category {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}
</style>
