<template>
  <AlertModal v-if="isModal.isOpen.value" @close="isModal.close()" :status="status" />
  <div v-else class="container">
    <div class="card">
      <!-- 제목 -->
      <h4>카테고리 등록</h4>
      <!-- input 그룹 -->
      <div class="input-group">
        <input v-model="name" type="text" placeholder="브랜드 상호명" />
        <input v-model="diary" type="text" placeholder="개월" />
      </div>
      <button @click="addCategory">
        <v-icon>mdi-plus</v-icon>
        <span>브랜드 추가하기</span>
      </button>
    </div>

    <div class="content">
      <table>
        <thead>
          <tr>
            <th>제품 브랜드</th>
            <th>유통기한(개월)</th>
            <th>지우기</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(item, index) in categoryStore.categoryList" :key="index">
            <tr>
              <td>{{ item.name }}</td>
              <td>{{ item.diary }}</td>
              <td><button type="button" @click="deleteCategory(item.id)">x</button></td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { authInstance } from '@/api/authApi'
import { useCategory } from '@/stores/category'
import { useModal } from '@/util/useModal'

const name = ref(null)
const diary = ref(null)
const categoryStore = useCategory()

// 카테고리 삭제
async function deleteCategory(index) {
  try {
    console.log(index)
    const response = await authInstance('/products/category').delete(`/${index}`)
    categoryStore.categoryList = categoryStore.categoryList.filter(
      (category) => category.id !== index
    )
    console.log('선택', response)
  } catch (error) {
    console.error(error)
  } finally {
    // isModal.open()
    // // 모달 닫기
    // setTimeout(() => {
    //   isModal.close()
    // }, 1500)
  }
}

// 성공여부
const isModal = useModal()
const status = ref('success')
const emit = defineEmits(['close'])

const addCategory = async () => {
  const data = {
    name: name.value,
    diary: diary.value
  }
  try {
    const response = await authInstance('/category').post('', data)
    categoryStore.categoryList.push({
      name: name.value,
      diary: diary.value,
      id: response.data.id
    })
  } catch (error) {
    status.value = 'fail'
  } finally {
    isModal.open()
    // 모달 닫기
    setTimeout(() => {
      isModal.close()
      emit('close')
    }, 1000)
  }
}
</script>

<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  gap: 20px;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25);

  input {
    width: 9.5rem;
    height: 40px;
    border-radius: 8px;
    border: 1px solid #ddd;
    padding: 1rem;
  }
  button {
    height: 40px;
    border-radius: 8px;
    border: 1px solid #ddd;
    cursor: pointer;
    transition:
      background-color 0.3s,
      transform 0.3s;
  }
  button.active {
    background-color: #0056b3;
  }
}
.input-group {
  display: flex;
  justify-content: center;
  gap: 6px;
}
table {
  width: 100%;
  margin-top: 20px;
}
td {
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  background: #fff;
  text-align: center;
}
thead {
  font-weight: bold;
  color: #fff;
  background: #73685d;
}
.content {
  min-height: 100vh;
  overflow-y: auto;
}
</style>
