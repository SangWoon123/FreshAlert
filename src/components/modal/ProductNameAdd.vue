<template>
  <v-card class="mx-auto product-card" width="344">
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
      <v-btn color="primary" @click="submit">등록</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { authInstance } from '@/api/authApi'
import { ref } from 'vue'
const emit = defineEmits(['close'])

const name = ref('')

async function submit() {
  // 제품명 등록
  await authInstance('/product-name').post('', {
    name: name.value
  })
  // 모달 닫기
  emit('close')
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
