<template>
  <v-card style="z-index: 1">
    <v-layout>
      <v-app-bar color="green" prominent>
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>재고파악</v-toolbar-title>

        <v-spacer></v-spacer>

        <template v-if="$vuetify.display.mdAndUp">
          <v-btn icon="mdi-magnify" variant="text"></v-btn>

          <v-btn icon="mdi-filter" variant="text"></v-btn>
        </template>
      </v-app-bar>

      <v-navigation-drawer
        width="150"
        v-model="drawer"
        :location="$vuetify.display.mobile ? 'right' : undefined"
        temporary
      >
        <v-list>
          <v-list-item v-for="item in items" :key="item.value" @click="selectCategory(item.value)">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </v-card>
</template>

<script setup>
import { ref, watch } from 'vue'

const emit = defineEmits(['categoryChanged'])
const selectCategory = (category) => {
  emit('categoryChanged', category)
  drawer.value = false
}

const items = [
  {
    title: '홈',
    value: 'home'
  },
  {
    title: '카테고리 추가',
    value: 'category'
  }
]

const drawer = ref(false)
const group = ref(null)

watch(group, () => {
  drawer.value = false
})
</script>
