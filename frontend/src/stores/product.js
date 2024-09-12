import { defineStore } from 'pinia'

export const useProductList = defineStore('product-list', {
  state: () => ({
    productList: []
  }),
  actions: {
    updateList(product) {
      this.productList.push(product)
    }
  }
})
