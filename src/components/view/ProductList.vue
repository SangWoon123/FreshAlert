<template>
  <div class="product">
    <h2>재고파악</h2>
    <div class="search">
      <v-text-field density="compact" variant="outlined"> </v-text-field>
      <v-btn color="green">검색</v-btn>
    </div>
    <div class="nav">
      <span>제품명</span>
      <span>유통기한</span>
      <span>개수</span>
      <span>꺼냄여부 ✅</span>
    </div>
    <v-divider thickness="3px"></v-divider>
    <div class="list">
      <div v-for="(item, index) in items" :key="index" class="list-item">
        <span :style="style(index)">{{ item.name }}</span>
        <span :style="style(index)">{{ item.expiry }}</span>
        <span :style="style(index)">{{ item.quantity }}</span>
        <input type="checkbox" v-model="item.checked" />
      </div>
    </div>

    <div class="footer">
      <v-btn color="green" variant="outlined">유통기한 등록</v-btn>
      <v-btn color="green">제품명 등록</v-btn>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { name: '[서울우유] 동서플레인요거트', expiry: '2024.10.25', quantity: 5, checked: false },
  { name: '[매일유업] 소프트요거트', expiry: '2024.09.30', quantity: 3, checked: false }
])
const style = (index) => {
  return {
    textDecoration: items.value[index].checked ? 'line-through' : 'none'
  }
}
</script>

<style lang="scss" scoped>
.product {
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  position: relative;
  h2 {
    margin-bottom: 20px;
  }
  .search {
    display: flex;
    gap: 10px;
  }

  .nav {
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding-bottom: 10px;
    :nth-child(1) {
      display: flex;
      justify-content: center;
      flex: 2;
    }
    :nth-child(2) {
      display: flex;
      justify-content: center;
      flex: 5;
    }
    :nth-child(3) {
      display: flex;
      flex: 1;
    }
  }

  .list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    overflow-y: auto;
    max-height: 90%;
    :nth-child(1) {
      display: flex;
      justify-content: center;
      flex: 2;
    }
    :nth-child(2) {
      display: flex;
      justify-content: center;
      flex: 4;
    }
    :nth-child(3) {
      display: flex;
      flex: 1;
    }
    :nth-child(4) {
      display: flex;
      flex: 1;
    }
    .list-item {
      font-size: 12px;
      display: flex;
      gap: 10px;
      padding: 5px;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #ddd;
      color: black;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
  }

  .footer {
    width: 100%;
    height: 70px;
    position: fixed;
    bottom: 0;
    left: 0;

    border-top: 1px solid #ddd;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
}
</style>
