<template>
  <AlertModal v-if="isModal.isOpen.value" :status="status" type="delete" :error-message="errorMessage" />
  <div v-else class="card">
    <div class="header">
      <h2>제품 삭제</h2>
    </div>

    <table>
      <thead>
        <tr>
          <th>제품명</th>
          <th>선택</th>
        </tr>
      </thead>
    </table>
    <div class="table-container">
      <table>
        <tbody>
          <tr v-for="(item, index) in productList.productNameList" :key="index" class="item">
            <td>{{ item.name }}</td>
            <td><input type="checkbox" :value="item.id" v-model="selectedIds" /></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="bottom">
      <v-btn variant="outlined" @click="$emit('close')">취소</v-btn>
      <v-btn color="red" @click="removeDelete">삭제</v-btn>
    </div>
  </div>
</template>

<script setup>
import { deleteProductName } from '@/api/authApi'
import { ref } from 'vue'
import { useProductList } from '../../stores/product'
import { useModal } from '@/util/useModal'
import AlertModal from '../AlertModal.vue'
defineEmits(['close'])

// 삭제여부
const status = ref('success')
const errorMessage = ref('')
const isModal = useModal()

const productList = useProductList()
const selectedIds = ref([])

async function removeDelete() {
  try {
    // 선택된 모든 ID에 대해 삭제 요청
    for (const id of selectedIds.value) {
      await deleteProductName(`/${id}`).delete('')
    }
    // 삭제 후 선택된 ID 배열로 제품명 목록 갱신
    productList.productNameList = productList.productNameList.filter(
      (item) => !selectedIds.value.includes(item.id)
    )
    // 선택된 ID 배열 초기화
    selectedIds.value = []
  } catch (error) {
    status.value = 'fail'
    if (error.response.status === 500) {
      errorMessage.value = '삭제할 수 없는 데이터가 존재합니다.'
    }
  } finally {
    isModal.open()
    // 모달 닫기
    setTimeout(() => {
      isModal.close()
    }, 1500)
  }
}
</script>

<style lang="scss" scoped>
.card {
  width: 100%;
  height: 60%;
  background-color: white;
  border-radius: 8px;
  padding: 1rem;
  position: relative;
}
.header {
  display: flex;
  justify-content: space-between;
}
.navigation {
  margin-top: 15px;
  display: flex;
  justify-content: space-around;
}
.bottom {
  position: absolute;
  bottom: 20px;
  right: 20px;
  display: flex;
  justify-content: end;
  gap: 14px;
}

table {
  border: 1px #a39485 solid;
  font-size: 0.9em;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25);
  width: 100%;
  border-collapse: collapse;
  border-radius: 5px;
  overflow: hidden;
}
th {
  text-align: left;
}

thead {
  font-weight: bold;
  color: #fff;
  background: #73685d;
}

td,
th {
  padding: 1em 0.5em;
  vertical-align: middle;
}

td {
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  background: #fff;
}

.table-container {
  overflow-y: auto;
  max-height: 70%;
}
</style>
