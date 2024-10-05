<template>
  <div class="product">
    <LoadingPage v-if="isLoading" />
    <div v-else>
      <!-- 헤더 -->
      <div class="header">
        <h2>재고파악</h2>
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
        <CustomButton
          color="#3E8F88"
          icon
          name="유통기한"
          type="추가하기"
          @click="openDiaryModal"
        />
        <CustomButton
          color="#3E8F88"
          icon
          name="제품명"
          type="추가하기"
          @click="openProductModal"
        />
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
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import ProductNameAdd from '../modal/ProductNameAdd.vue'
import LoadingPage from '@/components/view/Loading.vue'
import DiaryProductAdd from '../modal/DiaryProductAdd.vue'
import DiaryProductDelete from '../modal/DiaryProductDelete.vue'
import CustomButton from '../CustomButton.vue'
import { useModal } from '@/util/useModal'
import { authInstance } from '@/api/authApi'
import { useProductList } from '@/stores/product'
import { onMounted } from 'vue'

// 로딩
const isLoading = ref(true)
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

// 오늘 날짜 + 1일을 계산하는 함수
const getTomorrow = () => {
  const today = new Date()
  today.setDate(today.getDate() + 1)
  return today.toISOString().split('T')[0]
}

// 제품의 만료일이 내일인 경우만 셀력션 활성화
const isChecked = (expiration) => {
  return expiration !== getTomorrow()
}

// 검색
const searchQuery = ref('')
// 검색어 필터링 추가 및 날짜 변화지점 확인
const filteredProductList = computed(() => {
  let previousDate = null
  return productStore.productList
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

onMounted(async () => {
  try {
    // 유통기한 리스트 가져오기
    const response = await authInstance('/products').get('')
    productStore.productList = response.data
    // 제품명 리스트
    const productNames = await authInstance('/products-name').get('')
    productStore.productNameList = productNames.data
    // 날짜 리스트
    productStore.updateDateList()
  } catch (error) {
    console.error('데이터 로드 실패:', error)
  } finally {
    isLoading.value = false
  }
})
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
  }
  h2 {
    margin-bottom: 20px;
  }
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
</style>
