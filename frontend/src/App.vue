<template>
  <div class="layout-container">
    <nav v-if="authStore.isAuthenticated" class="navbar">
      <div class="nav-content">
        <span class="logo">🛠️ OS Ordem de Serviço</span>
        <div class="nav-links">
          <RouterLink to="/" class="link">Dashboard</RouterLink>
          <!-- <RouterLink to="/ordem-servico" class="link">Ordens de Serviço</RouterLink> -->
          <button @click="handleLogout" class="btn-sair">Sair</button>
        </div>
      </div>
    </nav>

    <div class="content-wrapper">
      <RouterView />
    </div>
  </div> </template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.layout-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
}

.navbar {
  background-color: #2c3e50;
  color: white;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo { font-weight: bold; font-size: 1.2rem; }

.nav-links { display: flex; gap: 20px; align-items: center; }

.link { color: #ecf0f1; text-decoration: none; font-weight: 500; }

.link:hover { color: #42b983; }

.btn-sair {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 5px 15px;
  border-radius: 4px;
  cursor: pointer;
}

.content-wrapper {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
}
</style>