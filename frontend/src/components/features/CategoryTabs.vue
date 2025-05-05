<template>
  <v-tabs bg-color="deep-purple-darken-4" center-active>
    <div v-for="(item, index) in categoryList" :key="index">
      <v-tab>
        <CategoryButton v-model="selectedCategory" :item="item" />
      </v-tab>
    </div>
  </v-tabs>
</template>

<script setup>
import { ref } from 'vue'
import { useCategory } from '@/stores/category'
import CategoryButton from './CategoryButton.vue';

const categoryStore = useCategory()
const categoryList = categoryStore.categoryList
const selectedCategory = ref(null)
</script>
