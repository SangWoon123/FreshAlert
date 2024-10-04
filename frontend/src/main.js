import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createVuetify } from 'vuetify/lib/framework.mjs'
import '@mdi/font/css/materialdesignicons.css'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { VDateInput } from 'vuetify/labs/VDateInput'
import App from './App.vue'
import router from './router'
import '@/assets/font.css'
import { ko } from 'vuetify/locale'
import VueGtag from 'vue-gtag'

const app = createApp(App)

const vuetify = createVuetify({
  locale: {
    locale: 'ko',
    messages: { ko }
  },
  components: {
    ...components,
    directives,
    VDateInput
  },
  ssr: true,
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
app.use(
  VueGtag,
  {
    config: { id: import.meta.env.VITE_GOOGLE_ANALYTICS }
  }
)


app.mount('#app')
