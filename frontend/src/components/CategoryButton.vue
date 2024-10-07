<template>
  <button
    :class="['container', isActive]"
    :style="{ backgroundColor: isActive ? 'cornflowerblue' : '#f5f5f5' }"
    @click="handleClick"
  >
    <span>{{ item.name }}</span>
  </button>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useCategory } from '@/stores/category'

const props = defineProps({
  item: {
    type: Object
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

const categoryStore = useCategory()
const isActive = computed(() => props.modelValue === props.item)

const isSelected = ref(props.modelValue)

const emit = defineEmits(['update:modelValue'])
const handleClick = () => {
  isSelected.value = !isSelected.value
  emit('update:modelValue', props.item)
  categoryStore.selectedCategory = props.item
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
.container.selected {
  background-color: #3e8f88;
}
</style>
