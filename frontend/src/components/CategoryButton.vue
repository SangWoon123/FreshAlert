<template>
  <button 
  class="container" 
  :style="{backgroundColor: isActive ? 'cornflowerblue' : '#f5f5f5'}"
  @click="handleClick">
    <img v-if="icon" width="20px" :src="getImageUrl(icon)" alt="icon" />
    <span>{{ name }}</span>
  </button>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  name: {
    type: String,
    default: '버튼'
  },
  icon: {
    type: String,
    default: null
  },
  modelValue: {
    type: String,
    default: ''
  }
})

const isActive = computed(() => props.modelValue === props.name)

const emit = defineEmits(['update:modelValue'])
const handleClick = () => {
  emit('update:modelValue', props.name)
}

const getImageUrl = (icon) => {
  return new URL(`../assets/${icon}.png`, import.meta.url).href
}
</script>

<style lang="scss" scoped>
.container {
  cursor: pointer;
  margin-top: 10px;
  margin-bottom: 18px;
  width: 80px;
  height: 30px;
  border: 1px solid #ddd;
  color: black;
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  border-radius: 8px;
}
</style>
