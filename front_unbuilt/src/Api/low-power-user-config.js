import {httpInstance} from '@/Api/httpInstance'

export default {
  getLowPowerUsers: function (params) {
    return httpInstance.post('/manage/lowpowerusertable', params)
  },
  insertLowPowerUser: function (params) {
    return httpInstance.post('/manage/lowpowerusers', params)
  },
  lowpoweruserDelete: function (params) {
    return httpInstance.post('/manage/lowpowerusersdelete', params)
  }
}
