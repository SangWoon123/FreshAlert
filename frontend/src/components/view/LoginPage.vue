<template>
  <div class="login">
    <LoadingPage v-if="isLoading" />

    <div v-else class="login__content">
      <div class="login__field">
        <h2>로그인</h2>

        <v-text-field
          label="번호를 입력하세요"
          variant="solo-filled"
          density="compact"
          class="login__input"
          v-model="code"
        ></v-text-field>
        <v-btn variant="outlined" class="login__button" color="#3e8f88" @click="auth">로그인</v-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingPage from '@/components/view/Loading.vue'
import router from '@/router'
import { authInstance } from '@/api/authApi'

const isLoading = ref(true)
const code = ref('')

async function auth() {
  try {
    // 로그인 검증 로직 추가
    const response = await authInstance('/login').post('', {
      code: code.value
    })

    if (response.status === 200) {
      router.push('/product')
    }
  } catch (error) {
    console.error('로그인 오류:', error.response ? error.response.data : error.message)
  }
}

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false
  }, 500)
})
</script>

<style lang="scss" scoped>
.login {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #3e8f88;
  padding: 10px;

  &__content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    max-width: 400px;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
    border-radius: 8px;
  }

  &__field {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
    width: 100%;
  }

  &__input {
    width: 100%;
  }

  &__button {
    width: 100%;
  }
}
</style>
