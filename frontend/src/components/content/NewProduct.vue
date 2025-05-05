<template>
  <div>
    <div class="toolbar">
      <v-btn flat icon>
        <v-icon>mdi-arrow-left</v-icon>
      </v-btn>
      <p class="toolbar-title">재고 파악</p>
      <div class="toolbar-actions">
        <v-btn flat icon @click="refreshPage">
          <v-icon>mdi-refresh</v-icon>
        </v-btn>
        <v-btn flat icon @click="openEmailModal">
          <v-icon color="red">mdi-alert-circle</v-icon>
        </v-btn>
      </div>
    </div>

    <!-- 검색창 -->
    <div>
      <v-text-field v-model="searchQuery" label="검색" density="compact" variant="outlined">
      </v-text-field>
    </div>

    <div style="height: 100vh; display: flex; flex-direction: column; padding-bottom: 80px">
      <div
        v-if="isLoading"
        style="display: flex; justify-content: center; align-items: center; height: 60vh"
      >
        <v-progress-circular indeterminate color="primary" />
      </div>
      <div v-else style="flex: 1; overflow-y: auto">
        <table>
          <thead>
            <tr>
              <th style="width: 45%">제품명</th>
              <th style="width: 35%">유통기한</th>
              <th style="width: 20%">남은 일수</th>
            </tr>
          </thead>
          <tbody>
            <template v-for="(item, index) in filteredProductList" :key="index">
              <tr v-if="item.isNewDate" class="date-row">
                <td colspan="3" class="date-cell">
                  <v-icon color="primary" small style="vertical-align: middle">mdi-calendar</v-icon>
                  <span style="margin-left: 6px">{{ item.expiration }}</span>
                </td>
              </tr>
              <tr class="list">
                <td style="text-align: left">{{ item.name }}</td>
                <td>{{ item.expiration }}</td>
                <td>
                  <span
                    :class="{
                      expired: getRemainDays(item.expiration) < 0,
                      warning:
                        getRemainDays(item.expiration) >= 0 && getRemainDays(item.expiration) <= 2
                    }"
                  >
                    {{ getRemainDaysText(item.expiration) }}
                  </span>
                </td>
              </tr>
            </template>
            <tr v-if="filteredProductList.length === 0">
              <td colspan="3" style="text-align: center; color: #aaa">검색 결과가 없습니다.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div :class="['footer', { expanded: changeInput }]" style="z-index: 10">
      <div v-if="!changeInput" style="display: flex; gap: 20px">
        <v-btn
          flat
          variant="outlined"
          rounded="lg"
          width="150px"
          height="50px"
          @click="changeFooter"
        >
          <v-icon>mdi-package-variant</v-icon>
          제품 관리
        </v-btn>
        <v-btn
          flat
          variant="outlined"
          width="150px"
          height="50px"
          @click="changeFooter('expiryRegistration')"
        >
          <v-icon>mdi-calendar-clock</v-icon>
          유통기한 등록
        </v-btn>
      </div>
      <template v-else>
        <ExpiryRegistration
          v-if="selectedAction === 'expiryRegistration'"
          @close="changeFooter('')"
        />
        <ProductManagement @close="changeFooter('')" v-else />
      </template>
    </div>
  </div>
  <EmailModal :isOpen="isEmailModalOpen" @close="closeEmailModal" />
</template>

<script setup>
import { useProductList } from '@/stores/product'
import ExpiryRegistration from './ExpiryRegistration.vue'
import ProductManagement from './ProductManagement.vue'
import { computed, onMounted, ref } from 'vue'
import { getProductNames, getProducts } from '@/api/authApi'
import EmailModal from '@/components/modals/EmailModal.vue'

const changeInput = ref(false)
const selectedAction = ref('')
const productStore = useProductList()
const isLoading = ref(true)
const searchQuery = ref('')

const isEmailModalOpen = ref(false)

const openEmailModal = () => {
  isEmailModalOpen.value = true
}

const closeEmailModal = () => {
  isEmailModalOpen.value = false
}

function changeFooter(action) {
  selectedAction.value = action
  changeInput.value = !changeInput.value
}

function refreshPage() {
  location.reload()
}

const filteredProductList = computed(() => {
  if (!searchQuery.value) return productStore.productList
  return productStore.productList.filter((item) =>
    item.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

// 남은 일수 계산 함수
function getRemainDays(expiration) {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  const exp = new Date(expiration)
  exp.setHours(0, 0, 0, 0)
  return Math.floor((exp - today) / (1000 * 60 * 60 * 24))
}
function getRemainDaysText(expiration) {
  const days = getRemainDays(expiration)
  if (days < 0) return '전날 만료'
  if (days === 0) return '당일 만료'
  if (days === 1) return 'D-1'
  if (days === 2) return 'D-2'
  return `D-${days}`
}

onMounted(async () => {
  try {
    // 유통기한 리스트 가져오기
    const response = await getProducts().get()
    productStore.productList = response.data
    // 제품명 리스트
    const productNames = await getProductNames('').get('')
    productStore.productNameList = productNames.data
    // 날짜 리스트
    productStore.updateDateList()
    // 카테고리 리스트
  } catch (error) {
    console.error('데이터 로드 실패:', error)
  } finally {
    isLoading.value = false
  }
})
</script>

<style lang="scss" scoped>
.list {
  font-size: 15px;
  color: #222;
  font-family: 'Pretendard', 'Arial', sans-serif;
  transition: background 0.2s;
  &:hover {
    background: #f0f4f8;
  }
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
thead {
  background: #f8fafc;
  tr {
    th {
      text-align: left;
      padding: 12px 10px;
      font-weight: 600;
      color: #3e8f88;
      font-size: 14px;
      border-bottom: 1px solid #e0e0e0;
    }
  }
}

tbody {
  tr {
    td {
      padding: 12px 10px;
      text-align: left;
      border-bottom: 1px solid #f0f0f0;
    }
  }
}
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
}

.toolbar-title {
  color: grey;
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
}

.toolbar-actions {
  display: flex;
  gap: 8px;
}

.v-btn {
  min-width: 40px !important;
  padding: 0 !important;
}
.footer {
  width: 100%;
  height: 80px;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 1;
  border-top: 1px solid #ddd;
  border-radius: 20px 20px 0 0;
  background-color: #ffffff;
  display: flex;
  justify-content: space-around;
  align-items: center;
  transition: height 0.5s ease;
}
.footer.expanded {
  height: 70vh;
}
.date-row {
  background: #f5f5f5;
}
.date-cell {
  text-align: left;
  font-size: 16px;
  color: #3f51b5;
  padding: 14px;
  font-weight: bold;
}
.expired {
  color: #e53935;
  font-weight: bold;
}
.warning {
  color: #ff9800;
  font-weight: bold;
}
</style>
