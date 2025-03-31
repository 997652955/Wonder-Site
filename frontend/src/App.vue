<template>
  <div class="container">
    <div v-if="isLoading" class="loading-overlay">
      <div class="loader"></div>
      <p>正在加载数据...</p>
    </div>
    
    <div v-else-if="categories && categories.length">
      <header>
        <h1>一个神奇的网站</h1>
        <div class="search-box">
          <input v-model="searchQuery" placeholder="搜索网站..." />
        </div>
      </header>

      <div class="category" v-for="category in filteredCategories" :key="category.name">
        <h2>{{ category.name }}</h2>
        <div class="link-grid">
          <a 
            v-for="link in category.links" 
            :key="link.url"
            :href="link.url"
            target="_blank"
            class="link-card"
          >
            <div class="link-content">
              <img 
                v-if="link.icon" 
                :src="link.icon" 
                class="link-icon"
                loading="lazy"
                @error="handleImageError"
              />
              <h3>{{ link.title }}</h3>
              <p>{{ link.desc }}</p>
            </div>
          </a>
        </div>
      </div>
    </div>
    <div v-else class="error-message">
      <p>暂无数据显示</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categories: [],
      searchQuery: '',
      isLoading: true
    }
  },
  computed: {
    filteredCategories() {
      if (!this.categories) return []
      return this.categories.map(category => ({
        ...category,
        links: category.links.filter(link =>
          link.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          link.desc.toLowerCase().includes(this.searchQuery.toLowerCase())
        )
      })).filter(category => category.links.length > 0)
    }
  },
  async mounted() {
    try {
      console.log('开始请求数据...')
      console.log('API地址:', this.$http.defaults.baseURL)
      const response = await this.$http.get('/nav-links')
      console.log('获取数据成功:', response.data)
      if (Array.isArray(response.data)) {
        this.categories = response.data
      } else {
        console.error('返回数据格式错误:', response.data)
        this.categories = []
      }
    } catch (error) {
      console.error('请求失败:', error.message)
      console.error('请求配置:', error.config)
      console.error('响应状态:', error.response?.status)
      console.error('响应数据:', error.response?.data)
      this.categories = []
    } finally {
      this.isLoading = false
    }
  },
  methods: {
    handleImageError(event) {
      event.target.style.display = 'none'  // 隐藏损坏的图标
      // 或使用备用图标
      // event.target.src = '/default-icon.svg'
    }
  },
  errorCaptured(err, instance, info) {
    console.error('组件错误:', err)
    return false
  }
}
</script>

<style>
/* 确保body和html有完整高度 */
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  min-height: 100vh;
  color: #e1e1e1;
  -webkit-overflow-scrolling: touch; /* 优化iOS滚动 */
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', system-ui, sans-serif;
  min-height: 100vh;
  box-sizing: border-box;
}

.error-message {
  text-align: center;
  padding: 2rem;
  color: #fff;
}

header {
  text-align: center;
  margin-bottom: 3rem;
}

h1 {
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 1.5rem;
  font-weight: bold;
  text-shadow: 0 0 10px rgba(52, 152, 219, 0.5);
}

.search-box {
  max-width: 600px;
  margin: 0 auto;
}

.search-box input {
  width: 100%;
  padding: 1rem;
  border: 2px solid #2c3e50;
  border-radius: 2rem;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}

.search-box input:focus {
  outline: none;
  border-color: #00a8ff;
  box-shadow: 0 0 15px rgba(0, 168, 255, 0.3);
}

.search-box input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.category {
  margin-bottom: 3rem;
}

.category h2 {
  font-size: 1.8rem;
  color: #00a8ff;
  border-left: 4px solid #00a8ff;
  padding-left: 1rem;
  margin-bottom: 1.5rem;
  text-shadow: 0 0 5px rgba(0, 168, 255, 0.3);
}

.link-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}

.link-card {
  display: block;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s ease;
  text-decoration: none;
  color: #e1e1e1;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
}

.link-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 168, 255, 0.15);
  border-color: #00a8ff;
  background: rgba(255, 255, 255, 0.08);
}

.link-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.link-icon {
  width: 24px;
  height: 24px;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.link-content h3 {
  font-size: 1.2rem;
  margin: 0.5rem 0;
  color: #fff;
}

.link-content p {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 768px) {
  .container {
    padding: 1rem 0.5rem;
    overflow-x: hidden; /* 防止水平滚动 */
  }
  
  .link-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 0 0.5rem;
  }
  
  .category {
    margin-bottom: 2rem;
    padding: 0 0.5rem;
    overflow: hidden; /* 防止内容溢出 */
  }
  
  .link-card {
    padding: 1rem;
    min-height: 100px;
    touch-action: manipulation;
  }
  
  h1 {
    font-size: 2rem;
    padding: 0 1rem;
  }
  
  .search-box {
    padding: 0 1rem;
  }

  .search-box input {
    font-size: 1rem;
    padding: 0.8rem;
    width: calc(100% - 2rem);  /* 考虑padding */
    -webkit-appearance: none;
    appearance: none;
    border-radius: 2rem;
  }

  .category h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }

  .link-content h3 {
    font-size: 1.1rem;
  }

  .link-content p {
    font-size: 0.9rem;
  }

  /* 优化触摸体验 */
  .link-card {
    -webkit-tap-highlight-color: transparent;
  }

  /* 适配刘海屏 */
  .container {
    padding-top: env(safe-area-inset-top);
    padding-bottom: env(safe-area-inset-bottom);
  }
}

/* 适配深色模式 */
@media (prefers-color-scheme: dark) {
  body {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  }
}

.loading-overlay {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
}

.loader {
  border: 4px solid rgba(255, 255, 255, 0.1);
  border-top: 4px solid #00a8ff;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  margin: 0 auto 1rem;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style> 