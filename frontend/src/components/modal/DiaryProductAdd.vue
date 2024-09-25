<template>
  <AlertModal v-if="isModal.isOpen.value" @close="isModal.close()" :status="status" />
  <div v-else class="card">
    <v-row d-flex justify="center">
      <v-col cols="12" lg="6" md="8" sm="10">
        <v-card ref="form">
          <div class="title">
            <h3>유통기한 제품</h3>
            <span>입고된 유통기한 제품을 등록하세요</span>
          </div>
          <v-card-text>
            <h4>제품</h4>
            <div class="search-container">
              <input class="search-input" type="text" placeholder="제품명" v-model="searchQuery" />
              <!-- 검색결과 -->
              <div class="search" v-if="!selectedProduct">
                <div v-for="(item, index) in filterProductNameList" :key="index">
                  <div class="search-item" @click="selectProduct(item)">{{ item.name }}</div>
                </div>
              </div>
            </div>
            <h4>유통기한 날짜</h4>
            <!-- 달력 -->
            <div class="date">
              <CustomSelect :options="['2024', '2025']" placeholder="년" v-model="selectedYear" />
              <CustomSelect
                :options="['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']"
                placeholder="월"
                v-model="selectedMonth"
              />
              <CustomSelect :options="day" placeholder="일" v-model="selectedDay" />
            </div>
            <h4>개수</h4>
            <input
              type="number"
              placeholder="개수"
              class="search-input"
              v-model="selectedQuantity"
            />
          </v-card-text>
          <v-divider class="mt-12"></v-divider>
          <v-card-actions>
            <!-- 버튼 -->
            <v-btn variant="text" @click="$emit('close')"> 취소 </v-btn>
            <v-spacer></v-spacer>

            <v-btn color="green" variant="text" @click="add"> 등록 </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { authInstance } from '@/api/authApi'
import { computed, onMounted, ref } from 'vue'
import { dateUtil } from '@/util/dateUtil'
import { useProductList } from '@/stores/product'
import CustomSelect from '../CustomSelect.vue'
import { useModal } from '../../util/useModal'
import AlertModal from '../AlertModal.vue'

// 등록성공 여부 상태값
const isModal = useModal()
const status = ref('success')

// 현재모달 상태 close
const emit = defineEmits(['close'])

const searchQuery = ref('')
const productList = useProductList()

const filterProductNameList = computed(() => {
  if (!searchQuery.value) {
    return productList.productNameList
  }
  const query = searchQuery.value.toLocaleLowerCase()
  return productList.productNameList.filter((item) => item.name.toLocaleLowerCase().includes(query))
})

function selectProduct(item) {
  searchQuery.value = item.name
  selectedProduct.value = item.id
}

// 제품명, 개수, 유통기한 상태 관리
const productNames = ref([])
const selectedProduct = ref(null)
const selectedQuantity = ref(null)
// 년월일
const selectedYear = ref(null)
const selectedMonth = ref(null)
const selectedDay = ref(null)
const day = dateUtil().totalDay()
const date = computed(() => `${selectedYear.value}-${selectedMonth.value}-${selectedDay.value}`)
// 상태관리
const productStroe = useProductList()

async function add() {
  try {
    const response = await authInstance('/product').post('', {
      name_id: selectedProduct.value,
      quantity: selectedQuantity.value,
      expiration: date.value
    })

    const expiration = dateUtil().showDate(date.value)

    const data = {
      name: productNames.value.filter((product) => product.id === selectedProduct.value)[0].name,
      quantity: selectedQuantity.value,
      expiration: expiration,
      checked: false
    }

    // 유통기한이 동일한 제품 목록을 찾음
    const sameExpirationIndex = productStroe.productList.findIndex(
      (product) => product.expiration === expiration
    )
    // 유통기한이 동일한 항목이 있으면 그 뒤에 추가, 없으면 그냥 마지막에 추가
    if (sameExpirationIndex !== -1) {
      // 유통기한이 동일한 항목 뒤에 추가
      productStroe.productList.splice(sameExpirationIndex, 0, data)
    } else {
      // 유통기한이 동일한 항목이 없으면 그냥 마지막에 추가
      productStroe.productList.push(data)
    }
  } catch (error) {
    console.error('유제품 등록 실패: ', error)
    status.value = 'fail'
  } finally {
    // 성공 메시지
    isModal.open()

    // 모달 닫기
    setTimeout(() => {
      isModal.close()
      emit('close')
    }, 1000)
  }
}

onMounted(async () => {
  const response = await authInstance('/products-name').get()
  productNames.value = response.data.map((item) => item)
})
</script>

<style scoped lang="scss">
.title {
  padding: 1rem;
  padding-bottom: 0;
  color: #3e8f88;
  span {
    color: darkgray;
    font-size: 12px;
  }
}
.card {
  width: 100%;
  padding: 1rem;
}
.date {
  display: flex;
  justify-content: center;
  gap: 10px;
}
.search-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}
.search-input {
  width: 100%;
  height: 50px;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ddd;
}
.search {
  width: 100%;
  height: 200px;
  max-height: 200px;
  overflow-y: auto;
  margin-bottom: 10px;
  box-shadow: 0px 1px 0px 1px lightgrey;
}
.search-item {
  width: 100%;
  padding: 1rem;
  border-top: 1px solid #ddd;
  color: #757575;
  cursor: pointer;
}
</style>
