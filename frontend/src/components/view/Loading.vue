<script setup></script>

<template>
  <div class="loading">
    <div class="loading__logo">
      <div>
        <span>작지만 강한 친구</span>
        <h2>스몰벗 유제품 기한</h2>
      </div>
    </div>
  </div>
</template>

<style scope lang="scss">
.loading {
  height: 100%;
  background: #3e8f88;
  background-size: 30px 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  &__logo {
    width: 100%;
    height: 30%;
    display: flex;
    justify-content: center;
    align-items: center;
    h2,
    div {
      color: white;
    }
    span {
      color: #616870;
    }
  }
}
</style>
