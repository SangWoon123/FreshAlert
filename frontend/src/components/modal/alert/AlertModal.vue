<template>
  <div :class="['card']">
    <!-- 아이콘 -->
    <div :class="['icon-content', statusClass]">
      <span v-if="status === 'success'" class="mdi mdi-check icon"></span>
      <span v-else class="mdi mdi-alert-circle-outline icon"></span>
    </div>
    <!-- 메시지 -->
    <div class="message" :style="{ color: status === 'success' ? '#74c4bd' : '#CE6C75' }">
      <h2>{{ message }}</h2>
      <div>{{ errorMessage }}</div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  status: {
    type: String,
    required: true
  },
  errorMessage: {
    type: String,
    required: false
  },
  type: {
    type: String,
    required: false,
    default: 'register'
  }
})

const message = computed(() => {
  // 삭제타입의 요청이 들어왔을때
  if (props.type === 'delete') {
    return props.status === 'success' ? '삭제완료' : '삭제실패'
  }
  // 등록타입의 요청이 들어왔을때
  return props.status === 'success' ? '등록완료' : '등록실패'
})
const statusClass = computed(() => {
  return props.status === 'success' ? 'success' : 'fail'
})
</script>

<style lang="scss" scoped>
@keyframes scaleUp {
  0% {
    transform: scale(0.5);
    opacity: 0;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 150px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  border-radius: 8px;
  padding: 1rem;
  position: relative;
  gap: 5px;
  background-color: white;
}
.icon-content {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  animation: scaleUp 0.5s ease-in-out;
}

.icon {
  font-size: 50px;
  color: white;
  animation: scaleUp 0.5s ease-in-out;
}
.message {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.success {
  color: #74c4bd;
  background-color: #74c4bd;
}

.fail {
  color: #ce6c75;
  background-color: #ce6c75;
}
</style>
