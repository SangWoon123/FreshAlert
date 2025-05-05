<template>
  <div class="loading">
    <div class="loading__logo">
      <p>잠시만 기다려주세요...</p>
      <v-progress-circular
        color="#4ed3b0"
        model-value="20"
        :size="75"
        :width="12"
        indeterminate
      ></v-progress-circular>
    </div>
  </div>
</template>

<style scope lang="scss">
.loading {
  height: 900px;
  background-size: 30px 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  &__logo {
    width: 100%;
    height: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    h2,
    div {
      color: white;
    }
    p {
      color: #616870;
    }
  }
}
</style>
