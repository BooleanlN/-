import {httpFileInstance} from '@/Api/httpInstance'
export default {
  postExcel: function (params) {
    return httpFileInstance.post('/api/excel', params)
  }
}
