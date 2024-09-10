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
        ></v-text-field>
        <v-btn variant="outlined" class="login__button" color="#3e8f88" @click="move">로그인</v-btn>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingPage from '@/components/view/Loading.vue'
import router from '@/router';

const isLoading = ref(true)

function move(){
  // 로그인 검증 로직 추가
  router.push('/product')
}

onMounted(() => {
  setTimeout(() => {
    isLoading.value = false
  }, 500) // 로딩 화면을 0.5초 동안 표시
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
