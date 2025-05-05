<template>
  <AlertModal
    style="position: absolute"
    v-if="isModal.isOpen.value"
    @close="isModal.close()"
    :status="status"
    :error-message="errorMessage"
  />
  <div class="expanded-content">
    <v-btn icon="mdi-close" class="close-btn" @click="$emit('close')"></v-btn>

    <div class="title">
      <h3>유통기한 제품</h3>
      <span>입고된 유통기한 제품을 등록하세요</span>
    </div>

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
      <button class="select-button" @click="inputDatePicker">
        <p>{{ inputDataDate }}</p>
        <v-icon>mdi-calendar-blank-outline</v-icon>
      </button>
    </div>

    <v-btn
      style="position: absolute; bottom: 0; left: 0"
      width="100%"
      height="80px"
      color="#3e8f88"
      @click="add"
    >
      등록
    </v-btn>

    <div v-if="datePicker" class="datepicker-overlay">
      <v-date-picker v-model="dateselect" @input="inputDatePicker" />
      <v-btn @click="selectedDate">선택</v-btn>
    </div>
  </div>
</template>

<script setup>
import { addProduct, getProductNames } from '@/api/authApi'
import { useProductList } from '@/stores/product'
import { computed, onMounted, ref } from 'vue'
import AlertModal from '@/components/modals/AlertModal.vue'
import { useModal } from '@/util/useModal'
import { dateUtil } from '@/util/dateUtil'

const searchQuery = ref('')
const datePicker = ref(false)
const dateselect = ref(new Date())
const inputDataDate = ref('')
const productList = useProductList()
const selectedProduct = ref(null)
const productStore = useProductList()

const isModal = useModal()
const status = ref('success')
const errorMessage = ref('')

function inputDatePicker() {
  datePicker.value = !datePicker.value
}

function selectedDate() {
  const selected = new Date(dateselect.value)
  const year = selected.getFullYear()
  const month = String(selected.getMonth() + 1).padStart(2, '0') // getMonth는 0부터 시작
  const day = String(selected.getDate()).padStart(2, '0')
  const formattedDate = `${year}-${month}-${day}`
  inputDataDate.value = formattedDate
  datePicker.value = false
}

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
const emit = defineEmits(['close'])
const productStroe = useProductList()

async function add() {
  if (!inputDataDate.value || !searchQuery.value) {
    alert('모든 항목을 입력해주세요.')
    return
  }

  try {
    await addProduct().post('/addProduct', {
      nameId: selectedProduct.value,
      expiration: inputDataDate.value
    })

    const expiration = dateUtil().showDate(inputDataDate.value)

    const data = {
      name: productStore.productNameList.filter(
        (product) => product.id === selectedProduct.value
      )[0].name,
      expiration: expiration
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
  try {
    const response = await getProductNames().get()
    productStore.productNameList = response.data
  } catch (error) {
    console.error('API Error:', error)
  }
})
</script>

<style lang="scss" scoped>
.expanded-content {
  padding: 0.5rem;
  width: 100%;
  height: 100%;
  margin: 0.5rem;
}

.title {
  padding: 1rem;
  padding-bottom: 0;
  color: #3e8f88;
  span {
    font-size: 12px;
  }
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}

.search-input {
  width: 100%;
  height: 50px;
  padding: 1rem;
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

.select-button {
  width: 100%;
  height: 50px;
  padding: 1rem;
  border-radius: 4px;
  border: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background-color: #ffffff;
  color: #757575;
  font-size: 16px;
  margin-bottom: 10px;
  box-shadow: 0px 1px 0px 1px lightgrey;
}

.search-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}

.datepicker-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>
