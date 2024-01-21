import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './routers.js'
import VueShortkey from 'vue3-shortkey';


const app = createApp(App)
app.config.compilerOptions.isCustomElement
app.use(VueShortkey)
app.use(router)
app.mount('#app')
