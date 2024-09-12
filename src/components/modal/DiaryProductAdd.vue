<template>
  <v-row d-flex justify="center">
    <v-col cols="12" lg="6" md="8" sm="10">
      <v-card ref="form">
        <v-card-text>
          <v-select
            label="제품명"
            :items="productNames"
            item-title="name"
            item-value="id"
            v-model="selectedProduct"
            variant="solo-filled"
          ></v-select>
          <v-date-input
            v-model="selectedDate"
            clear-icon
            label="유통기한"
            variant="solo-filled"
            width="350px"
          ></v-date-input>

          <v-text-field label="개수" variant="solo-filled" v-model="selectedQuantity">
          </v-text-field>
        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <!-- 버튼 -->
          <v-btn variant="text" @click="$emit('close')"> 취소 </v-btn>
          <v-spacer></v-spacer>

          <v-btn color="green" variant="text" @click="test"> 등록 </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script setup>
import { authInstance } from '@/api/authApi'
import { onMounted, ref } from 'vue'
import { dateUtil } from '@/util/dateUtil'
import { useProductList } from '@/stores/product'
const emit = defineEmits(['close'])

// 제품명, 개수, 유통기한 상태 관리
const productNames = ref([])
const selectedProduct = ref('')
const selectedQuantity = ref(0)
const selectedDate = ref(null)
// 상태관리
const productStroe = useProductList()

async function test() {
  const response = await authInstance('/product').post('', {
    name_id: selectedProduct.value,
    quantity: selectedQuantity.value,
    expiration: dateUtil().showDate(selectedDate.value)
  })
  productStroe.updateList({
    name: productNames.value.filter((product) => product.id === selectedProduct.value)[0].name,
    quantity: selectedQuantity.value,
    expiration: dateUtil().showDate(selectedDate.value),
    checked: false
  })

  if (response.status === 200) {
    emit('close')
  }
}

onMounted(async () => {
  const response = await authInstance('/products-name').get()
  productNames.value = response.data.map((item) => item)
  console.log(productStroe.productList)
})
</script>
