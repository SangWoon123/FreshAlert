<template>
  <div :class="['card']">
    <div :class="['icon-content', statusClass]">
      <span v-if="status === 'success'" class="mdi mdi-check icon"></span>
      <span v-else class="mdi mdi-alert-circle-outline icon"></span>
    </div>
    <h2 :style="{ color: status === 'success' ? '#74c4bd' : '#CE6C75' }">{{ message }}</h2>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  status: {
    type: String,
    required: true
  }
})

const message = computed(() => {
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
.close {
  font-size: 25px;
  align-self: flex-end;
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
