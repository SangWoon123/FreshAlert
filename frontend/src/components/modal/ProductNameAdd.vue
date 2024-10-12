<template>
  <AlertModal
    v-if="isModal.isOpen.value"
    @close="isModal.close()"
    :status="status"
    :error-message="errorMessage"
  />
  <v-card v-else class="mx-auto product-card" width="344">
    <v-card-titl color="green">
      <h2 style="color: #3e8f88">제품등록</h2>
    </v-card-titl>
    <v-card-text class="text-field-box">
      <v-text-field
        label="제품명을 입력하세요"
        variant="solo"
        density="compact"
        v-model="name"
      ></v-text-field>
    </v-card-text>

    <v-card-actions class="action-buttons">
      <v-btn color="red" @click="$emit('close')">취소</v-btn>
      <v-btn color="primary" @click="submit"> 등록 </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import AlertModal from './alert/AlertModal.vue'
import { authInstance } from '@/api/authApi'
import { useProductList } from '../../stores/product'
import { ref } from 'vue'
import { useModal } from '../../util/useModal'

// 등록상태 성공여부
const isModal = useModal()
const status = ref('success')
const errorMessage = ref('')

const emit = defineEmits(['close'])
const name = ref('')
async function submit() {
  if (!name.value) {
    return
  }
  try {
    // 제품명 등록
    const response = await authInstance('/product-name').post('', {
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

    // 모달 닫기
    setTimeout(() => {
      isModal.close()
      emit('close')
    }, 1500)
  }
}
</script>

<style lang="scss" scoped>
.product-card {
  color: white;
  padding: 16px;
  border-radius: 8px;
}

.text-field-box {
  display: flex;
  justify-content: center;
}

.action-buttons {
  display: flex;
  align-items: center;
  justify-content: end;
  width: 100%;
}

.v-btn {
  border-radius: 8px;
}
</style>
