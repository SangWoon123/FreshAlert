<template>
  <div class="app-email-modal" v-if="isOpen">
    <div class="app-email-modal-content">
      <h2>피드백 보내기</h2>
      <textarea
        v-model="content"
        placeholder="불필요하거나 필요한 기능에 대한 피드백을 작성해주세요."
        rows="5"
      ></textarea>
      <div class="app-email-modal-buttons">
        <button @click="sendRequestEmail" class="app-email-modal-send-button">보내기</button>
        <button @click="closeModal" class="app-email-modal-cancel-button">취소</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import emailjs from '@emailjs/browser'
const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['close'])

const content = ref('')

const sendRequestEmail = () => {
  const payload = {
    message: content.value,
    time: new Date()
      .toLocaleString('ko-KR', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      })
      .replace(/\./g, '-')
  }
  emailjs
    .send(
      import.meta.env.VITE_EMAILJS_SERVICE_ID,
      import.meta.env.VITE_EMAILJS_TEMPLATE_ID,
      payload,
      import.meta.env.VITE_EMAILJS_PUBLIC_KEY
    )
    .then((res) => {
      alert('피드백이 성공적으로 전송되었습니다.')
      closeModal()
      console.log(res)
    })
    .catch((err) => {
      alert('피드백 전송에 실패했습니다. 다시 시도해주세요.')
      console.error(err)
    })
}

const closeModal = () => {
  content.value = ''
  emit('close')
}
</script>

<style scoped>
.app-email-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.app-email-modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 90%;
  max-width: 500px;
}

h2 {
  margin-bottom: 20px;
  color: #333;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 20px;
  resize: vertical;
}

.app-email-modal-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
}

.app-email-modal-send-button {
  background-color: #4caf50;
  color: white;
}

.app-email-modal-cancel-button {
  background-color: #f44336;
  color: white;
}

button:hover {
  opacity: 0.9;
}
</style>
