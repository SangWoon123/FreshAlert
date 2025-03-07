<template>
  <div class="login">
    <div class="login__field">
      <h3 style="color: lightgrey">내가 담당해요</h3>
      <h1>스몰벗의 매장관리</h1>

      <div style="width: 100%; display: flex; align-items: center; justify-content: center">
        <input
          placeholder="매장 코드를 입력하세요"
          variant="solo-filled"
          v-model="code"
          type="password"
        />
        <v-btn @click="auth" flat>
          <v-icon> mdi-arrow-right-bold-outline </v-icon>
        </v-btn>
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 10px;

  &__content {
    display: flex;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
  input {
    width: 100%;
    padding: 10px;
    border: 1px solid lightgrey;
    border-radius: 5px;
    margin-right: 10px;
  }
}
</style>
