import {httpInstance} from '@/Api/httpInstance'

export default {
  getKnowledgeTable: function (params) {
    return httpInstance.post('/api/knowledgetable', params)
  },
  insertKnowledgeDatas: function (params) {
    return httpInstance.post('/api/knowledge', params)
  },
  deleteKnowledgeData: function (params) {
    return httpInstance.post('/api/knowledgedelete', params)
  }
}
