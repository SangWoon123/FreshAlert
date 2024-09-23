<template>
  <div class="custom-select">
    <div class="select-box" @click="modal.toggle()">
      <div class="selected-value">{{ `${selectedValue || ''} ${placeholder}` }}</div>
      <div class="arrow">&#9662;</div>
    </div>

    <div v-if="modal.isOpen" class="options">
      <div
        v-for="(option, index) in options"
        :key="index"
        class="option"
        :class="{ selected: option.value === selectedValue }"
        @click="selectOption(option)"
      >
        {{ option }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useModal } from '../util/useModal'

const props = defineProps({
  options: {
    type: Array,
    required: true
  },
  placeholder: {
    type: String,
    default: 'Select an option'
  }
})

const emit = defineEmits(['date'])
const selectedValue = ref(props.modelValue)

// 드롭다운 열고 닫기
const modal = ref(useModal())

// 옵션 선택
const selectOption = (option) => {
  selectedValue.value = option
  emit('update:modelValue', option)
  modal.value.close()
}
</script>

<style scoped>
.custom-select {
  position: relative;
  width: 200px;
  margin-bottom: 24px;
}

.select-box {
  border-radius: 8px;
  border: 1px solid #bbb;
  padding: 10px;
  background-color: #fff;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #757575;
}

.selected-value {
  font-size: 14px;
}
input::placeholder {
  color: #3e8f88;
}
.arrow {
  font-size: 12px;
}

.options {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  z-index: 10;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  max-height: 100px;
  overflow-y: auto;
}

.option {
  padding: 10px;
  cursor: pointer;
  font-size: 14px;
}

.option:hover {
  background-color: #f0f0f0;
}

.option.selected {
  background-color: #e0e0e0;
}
</style>
