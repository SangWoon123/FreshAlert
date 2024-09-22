<template>
  <div class="login">
    <div class="login__content">
      <div class="login__field">
        <h2>매니저 로그인</h2>

        <v-text-field
          label="코드를 입력하세요"
          variant="solo-filled"
          density="compact"
          class="login__input"
          v-model="code"
          type="password"
          flat
        ></v-text-field>
        <v-btn variant="outlined" class="login__button" color="#3e8f88" @click="auth">로그인</v-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import router from '@/router'
import { authInstance } from '@/api/authApi'

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
</script>

<style lang="scss" scoped>
.login {
  height: 939px; /* Z 플립의 높이에 맞춤 */
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
