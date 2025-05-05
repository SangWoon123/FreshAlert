<template>
  <AlertModal
    style="position: absolute"
    v-if="isModal.isOpen.value"
    @close="isModal.close()"
    :status="status"
    :error-message="errorMessage"
  />
  <div class="expanded-content">
    <v-btn icon="mdi-close" class="close-btn" @click="$emit('close')" />
    <div class="title">
      <h3>제품 관리</h3>
      <span>입고된 제품을 관리하세요</span>
    </div>

    <h4>제품</h4>
    <div class="search-container">
      <input class="search-input" type="text" placeholder="제품명" v-model="name" />
    </div>

    <v-btn
      style="position: absolute; bottom: 0; left: 0"
      width="100%"
      height="80px"
      color="#3e8f88"
      @click="addProduct"
    >
      등록
    </v-btn>
  </div>
</template>

<script setup>
import { addProductName } from '@/api/authApi'
import { useProductList } from '@/stores/product'
import { useModal } from '@/util/useModal'
import { ref } from 'vue'

const isModal = useModal()
const status = ref('success')
const emit = defineEmits(['close'])

const name = ref('')
const errorMessage = ref('')

async function addProduct() {
  if (!name.value) {
    alert('제품명을 입력해주세요.')
    return
  }

  try {
    // 제품명 등록
    const response = await addProductName().post('/addProductName', {
      name: name.value
    })
    if (response.status === 200) {
      //상태관리 업데이트
      useProductList().productNameList.push({
        name: response.data.name,
        id: response.data.id
      })
    }
  } catch (error) {
    console.error('제품 등록 오류: ', error)
    status.value = 'fail'

    // 제품명 중복 에러
    if (error.response.status === 500) {
      errorMessage.value = '제품명이 중복됩니다.'
      return
    }
    // 그외 에러
    errorMessage.value = error.response?.data?.message || '제품 등록 중 오류가 발생했습니다.' // 에러 메시지 추출
  } finally {
    // 성공 메시지
    isModal.open()
    name.value = ''

    // 모달 닫기
    setTimeout(() => {
      isModal.close()
      emit('close')
    }, 500)
  }
}
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
.search-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}
.search-input {
  width: 100%;
  height: 50px;
  padding: 1rem;
  border-radius: 4px;
  border: 1px solid #ddd;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
