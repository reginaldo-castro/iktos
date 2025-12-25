<template>
  <div class="login-container">
    <h2>Acesse sua conta</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="username" type="username" placeholder="Nome" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <br>
      <button type="submit">Entrar</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const authStore = useAuthStore()
const router = useRouter()

async function handleLogin() {
  const success = await authStore.login({ username: username.value, password: password.value })
  if (success) {
    router.push('/')
  } else {
    alert('Credenciais inválidas!')
  }
}
</script>

<style scoped>
.login-container { max-width: 300px; margin: 100px auto; display: flex; flex-direction: column; }
input { margin-bottom: 10px; padding: 8px; }
button { padding: 10px; margin-left: 60px; background: #42b983; color: white; border: none; cursor: pointer; }
</style>