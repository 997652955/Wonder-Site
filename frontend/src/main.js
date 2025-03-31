import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

const app = createApp(App)

// 根据当前环境选择API地址
const apiBaseURL = import.meta.env.PROD 
  ? 'https://licj.gyaznjoyn.serv00.net/api'
  : 'http://localhost:5001/api'

// 配置axios的baseURL
axios.defaults.baseURL = apiBaseURL

// 添加请求拦截器，打印请求信息
axios.interceptors.request.use(config => {
  console.log('请求URL:', config.url)
  console.log('完整URL:', config.baseURL + config.url)
  return config
})

// 添加响应拦截器用于调试
axios.interceptors.response.use(
  response => response,
  error => {
    console.error('API请求错误:', error.message)
    return Promise.reject(error)
  }
)

app.config.globalProperties.$http = axios
app.mount('#app') 