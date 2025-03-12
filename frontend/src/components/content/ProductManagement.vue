<template>
  <div class="expanded-content">
    <v-btn icon="mdi-close" class="close-btn" @click="$emit('close')" />
    <div class="title">
      <h3>제품 관리</h3>
      <span>입고된 제품을 관리하세요</span>
    </div>

    <h4>제품</h4>
    <div class="search-container">
      <input class="search-input" type="text" placeholder="제품명" v-model="searchQuery" />
    </div>

    <v-btn
      style="position: absolute; bottom: 0; left: 0"
      width="100%"
      height="80px"
      color="#3e8f88"
      @click="addProduct"
    >
      등록
    </v-btn>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const searchQuery = ref('')

function addProduct() {
  if (!searchQuery.value) {
    alert('제품명을 입력해주세요.')
    return
  }

  console.log('제품명:', searchQuery.value)
  searchQuery.value = ''
}
</script>

<style lang="scss" scoped>
.expanded-content {
  padding: 0.5rem;
  width: 100%;
  height: 100%;
  margin: 0.5rem;
}
.title {
  padding: 1rem;
  padding-bottom: 0;
  color: #3e8f88;
  span {
    font-size: 12px;
  }
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}
.search-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}
.search-input {
  width: 100%;
  height: 50px;
  padding: 1rem;
  border-radius: 4px;
  border: 1px solid #ddd;
}
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
