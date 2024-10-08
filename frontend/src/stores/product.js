import { defineStore } from 'pinia'

export const useProductList = defineStore('product-list', {
  state: () => ({
    // 기본유제품
    productList: [],
    categoryProductList: [],
    productNameList: [],
    // 날짜 모음
    dateList: []
  }),
  actions: {
    updateList(product) {
      this.productList.push(product)
    },
    updateDateList() {
      this.dateList = [...new Set(this.productList.filter((item) => item.expiration))]
    }
  }
})
