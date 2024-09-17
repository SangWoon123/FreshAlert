<template>
  <button
    type="button"
    class="container"
    :style="{ backgroundColor: color }"
    @click="emit('click')"
  >
    <div class="col1">
      <span v-if="icon" class="material-symbols-outlined">widgets</span>
      <span v-else class="material-symbols-outlined">remove</span>
    </div>
    <div class="col2">
      <div>{{ name }}</div>
      <div>{{ type }}</div>
    </div>
  </button>
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
  />
</template>

<script setup>
defineProps({
  icon: Boolean,
  color: String,
  name: String,
  type: String
})
const emit = defineEmits(['click'])
</script>

<style lang="scss" scoped>
.container {
  border: none;
  width: 120px;
  height: 45px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  color: white;
  .col1 {
    display: flex;
    align-self: center;
    span {
      font-size: 34px;
    }
  }
  .col2 {
    display: flex;
    flex-direction: column;
    align-items: start;
    :nth-child(1) {
      font-size: 12px;
    }
  }
}
.material-symbols-outlined {
  font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24;
}
.material-symbols-outlined {
  font-variation-settings:
    'FILL' 0,
    'wght' 400,
    'GRAD' 0,
    'opsz' 24;
}
</style>
