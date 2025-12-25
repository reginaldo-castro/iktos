import api from './api';

export default {
  listarTudo() {
    return api.get('ordens-servico/');
  },
  
  buscarDetalhes(id) {
    return api.get(`ordens-servico/${id}/detalhe/`);
  },
  
  buscarPorId(id) {
    return api.get(`ordens-servico/${id}/`);
  },

  buscarChecklistDaOS(osId) {
    return api.get(`ordens-servico-checklist/?ordem_servico=${osId}`);
  },

  atualizarItemChecklist(id, dados) {
    return api.patch(`ordens-servico-checklist/${id}/`, dados);
  }
};