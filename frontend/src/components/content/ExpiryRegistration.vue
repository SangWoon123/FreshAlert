<template>
  <div class="expanded-content">
    <v-btn icon="mdi-close" class="close-btn" @click="$emit('close')"></v-btn>

    <div class="title">
      <h3>유통기한 제품</h3>
      <span>입고된 유통기한 제품을 등록하세요</span>
    </div>

    <h4>제품</h4>
    <div class="search-container">
      <input class="search-input" type="text" placeholder="제품명" v-model="searchQuery" />
    </div>

    <h4>유통기한 날짜</h4>

    <!-- 달력 -->
    <div class="date">
      <button class="select-button" @click="inputDatePicker">
        <p>{{ inputDataDate }}</p>
        <v-icon>mdi-calendar-blank-outline</v-icon>
      </button>
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

    <div v-if="datePicker" class="datepicker-overlay">
      <v-date-picker v-model="dateselect" @input="inputDatePicker" />
      <v-btn @click="selectedDate">선택</v-btn>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const searchQuery = ref('')
const datePicker = ref(false)
const dateselect = ref(new Date())
const inputDataDate = ref('')

function inputDatePicker() {
  datePicker.value = !datePicker.value
}

function selectedDate() {
  const selected = new Date(dateselect.value)
  const year = selected.getFullYear()
  const month = String(selected.getMonth() + 1).padStart(2, '0') // getMonth는 0부터 시작
  const day = String(selected.getDate()).padStart(2, '0')
  const formattedDate = `${year}-${month}-${day}`
  inputDataDate.value = formattedDate
  datePicker.value = false
}

function addProduct() {
  if (!inputDataDate.value || !searchQuery.value) {
    alert('모든 항목을 입력해주세요.')
    return
  }

  console.log(inputDataDate.value, searchQuery.value)
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

.search-input {
  width: 100%;
  height: 50px;
  padding: 1rem;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.select-button {
  width: 100%;
  height: 50px;
  padding: 1rem;
  border-radius: 4px;
  border: 1px solid #ddd;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background-color: #ffffff;
  color: #757575;
  font-size: 16px;
  margin-bottom: 10px;
  box-shadow: 0px 1px 0px 1px lightgrey;
}

.search-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 18px;
}

.datepicker-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>
