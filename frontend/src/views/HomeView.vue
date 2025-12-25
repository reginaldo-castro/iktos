<template>
  <div class="dashboard">
    <h1>Ordens de Serviço</h1>
    
    <div v-if="loading">Carregando ordens...</div>
    
    <div v-else class="os-grid">
      <div v-for="os in ordens" :key="os.id" :class="['os-card', `bg-${os.status}`]">
        <div class="card-header">
          <h3>OS #{{ os.id }} - {{ os.descricao }}</h3>
          <span class="status-dot"></span>
        </div>
        <!-- <p><strong>Cliente:</strong> {{ os.cliente }}</p> -->
        <p><strong>Status:</strong> <span :class="os.status">{{ os.status }}</span></p>
        <button @click="$router.push(`/ordens-servico/${os.id}`)" class="btn-detalhes">
          Ver Detalhes
        </button> 
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import osService from '@/services/osService';

const ordens = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const response = await osService.listarTudo();
    ordens.value = response.data.results || response.data;
  } catch (error) {
    console.error("Erro ao carregar OS:", error);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
.dashboard h1 { margin-bottom: 1.5rem; }

.os-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.os-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  border-left: 5px solid #42b983;
  transition: transform 0.2s;
}

.os-card:hover {
  transform: translateY(-5px);
}

.os-card h3 { margin-top: 0; color: #2c3e50; }
.os-card p { margin: 5px 0; color: #666; }

.status-badge {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  text-transform: uppercase;
  background: #eee;
}
.aberto { background: #ffeaa7; color: #d35400; }
.concluido { background: #55efc4; color: #00b894; }

.btn-detalhes {
  margin-top: 1rem;
  width: 100%;
  padding: 8px;
  background: #2c3e50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>