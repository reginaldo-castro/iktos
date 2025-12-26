  <template>
    <div class="os-detalhes" v-if="os">
      <header class="os-header">
        <button @click="$router.push('/')" class="btn-voltar">← Voltar</button>
        <h1>OS #{{ os.id }}</h1>
        <span :class="['status-badge', os.status]">{{ os.status }}</span>
      </header>

      <div class="card-info">
        <label><strong>Descrição da Atividade:</strong></label>
        <p class="descricao-texto">{{ os.descricao }}</p>
      </div>

      <div class="card-info">
        <label><strong>Cliente:</strong></label>
        <p class="descricao-texto">{{ os.cliente }}</p>
      </div>

      <div v-if="os.status === 'aberto'">
        <button @click="pegarServico" class="btn-assumir">Iniciar este Serviço</button>
      </div>

      <div v-else-if="os.status === 'em_andamento'">
        <p>Você está executando esta OS.</p>
      </div>

      <section class="checklist-section">
        <h2>Itens de Verificação</h2>
        
        <div class="checklist-container">
          <div v-for="item in os.checklist" :key="item.id" class="checklist-item">
            <label class="checkbox-container">
              <input 
                type="checkbox" 
                v-model="item.concluido" 
                @change="salvarProgressoItem(item)"
                :disabled="os.status === 'concluida'"
              >
              <span class="checkmark"></span>
              <span :class="{ 'texto-desativado': os.status === 'concluida' }">
                {{ item.descricao }}
              </span>
            </label>
          </div>
        </div>
      </section>

      <div v-if="os.foto" class="foto-container">
        <h3>Foto da Execução:</h3>
        <img :src="os.foto" alt="Foto da OS" class="foto-preview" />
      </div>

      <section class="secao-conclusao" v-if="os.status !== 'concluido'">
        <hr />
        <div class="upload-container">
          <label class="btn-foto">
            📷 Tirar Foto Comprobatória
            <input type="file" @change="onFileChange" accept="image/*" capture="camera" hidden>
          </label>
          <p v-if="fotoSelecionada" class="feedback-foto">✅ Foto capturada: {{ fotoSelecionada.name }}</p>
        </div>

        <button 
          @click="finalizarOrdem" 
          class="btn-concluir-final"
          :disabled="!podeConcluir"
        >
          {{ carregando ? 'Enviando...' : 'Finalizar e Concluir OS' }}
        </button>
      </section>

    </div>
  </template>

  <script setup>
  import { ref, onMounted, onUnmounted, computed } from 'vue'
  import osService from '@/services/osService'
  import api from '@/services/api'

  const props = defineProps(['id'])
  const os = ref(null)
  const fotoSelecionada = ref(null)
  const carregando = ref(false)

  const podeConcluir = computed(() => {
    const checklistOk = os.value?.checklist.some(item => item.concluido)
    return checklistOk && fotoSelecionada.value && !carregando.value
  })

  const onFileChange = (e) => {
    const arquivo = e.target.files[0];
    if (arquivo) {
      fotoSelecionada.value = arquivo;
      console.log("Foto selecionada:", arquivo.name);
    }
  };

  const finalizarOrdem = async () => {
    carregando.value = true;
    const fd = new FormData();
    fd.append('foto', fotoSelecionada.value);
    fd.append('status', 'concluida');

    try {
      const response = await api.post(`ordens-servico/${props.id}/concluir/`, fd, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      alert("OS Concluída!");
      
      window.location.href = '/'; 
      
    } catch (error) {
      console.error("Erro Real:", error);
      const msg = error.response?.data?.detail || "Erro ao conectar com o servidor";
      alert("Erro: " + msg);
    } finally {
      carregando.value = false;
    }
  };

  const salvarProgressoItem = async (item) => {
    console.log("A guardar item ID:", item.id, "Estado", item.concluido);
    
    if (!item.id) {
      console.error("Erro: O item não tem um ID!");
      return;
    }

    try {
      await api.patch(`ordens-servico-checklist/${item.id}/`, { 
        concluido: item.concluido 
      });
      console.log(`Sucesso! Item ${item.id} agora é ${item.concluido}`);
    } catch (error) {
      console.error("Erro ao salvar na tabela ternária:", error.response?.data);
    }
  }
  const carregarOS = async () => {
    try {
      const response = await osService.buscarDetalhes(props.id)
     os.value = response.data
    } catch (error) {
      console.error("Erro ao carregar detalhes da OS:", error)
    }
  }
  let interval = null;

  onMounted(() => {
    carregarOS();

    interval = setInterval(() => {
      carregarOS();
    }, 10000); 
  });

  onUnmounted(() => {
    if (interval) clearInterval(interval);
  });

  const atualizarStatusChecklist = async (item) => {
    try {
      console.log(`Item ${item.id} alterado para: ${item.concluido}`)
    } catch (error) {
      alert("Erro ao salvar alteração")
    }
  }

  const pegarServico = async () => {
    try {
      await api.post(`ordens-servico/${os.value.id}/assumir/`);
      alert("Você assumiu a OS!");
      await carregarOS();
    } catch (error) {
      alert(error.response?.data?.detail || "Erro ao assumir OS");
    }
  }
  </script>

  <style scoped>
  .os-header { display: flex; align-items: center; gap: 15px; margin-bottom: 2rem; }
  .card-info { background: #fff; padding: 20px; border-radius: 8px; margin-bottom: 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
  .checklist-item {
    background: #fff;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #eee;
  }
  .texto-riscado { text-decoration: line-through; color: #999; }
  .status-badge { padding: 4px 12px; border-radius: 20px; font-weight: bold; text-transform: uppercase; }
  .aberto { background: #ffeaa7; color: #d35400; }
  .btn-voltar { padding: 8px 15px; border: 1px solid #ccc; background: white; border-radius: 4px; cursor: pointer; }

  .foto-preview {
    width: 100%;
    max-width: 100px; 
    height: auto;
    border: 1px solid #ddd;
    border-radius: 8px;
  }

  .texto-desativado {
    color: #999;
    text-decoration: none;
  }

  </style>