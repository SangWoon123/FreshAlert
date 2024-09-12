import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify/lib/framework.mjs'
import * as components from 'vuetify/components'
import { VDateInput } from 'vuetify/labs/VDateInput'
import App from './App.vue'
import router from './router'
import '@/assets/font.css'

const app = createApp(App)

const vuetify = createVuetify({
  components: {
    ...components,
    VDateInput
  },
  theme: {
    defaultTheme: 'custom',
    themes: {
      custom: {
        dark: false,
        colors: {
          green: '#3e8f88',
          red: '#C2546E'
        }
      }
    }
  }
})

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
