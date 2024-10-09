import { defineStore } from 'pinia'

export const useCategory = defineStore('category', {
  state: () => ({
    categoryList: [],
    selectedCategory: '' // 선택된 카테고리 객체
  }),
  actions: {
    updateList(category) {
      this.selectedCategory = category
    }
  }
})
